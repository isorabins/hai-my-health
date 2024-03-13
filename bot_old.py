import openai
import os
from crewai import Crew, Process, Task, Agent
import logging
from enum import Enum, auto
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

telegram_token = os.environ["TELEGRAM_TOKEN"]
openai.api_key = os.environ["OPENAI_TOKEN"]
openai_version = os.environ["OPENAI_VERSION"]

messages_list = []

initial_interviewer = Agent(
    role='initial_interviewer',
    goal=(
        "gather baseline health data from the user to create a database where their symptoms can"
        " be tracked and analyzed over time"
    ),
    verbose=True,
    memory=True,
    backstory=(
        "I am a symptom tracker, eager to help you improve your health and well-being."
        " Friendly, helpful, focused on privacy and making the user feel comfortable"
        " I don't diagnose, just collect information to help you track your symptoms."
    ),
    allow_delegation=True
)

daily_interviewer = Agent(
    role='daily_interviewer',
    goal=(
        "check in each day with the patient to gather data on their symptoms and how they are feeling"
        " see if there are any changes or new symptoms/medications to report"
        " update their file with new information"
    ),
    verbose=True,
    memory=True,
    backstory=(
        "I am a symptom tracker, eager to help you improve your health and well-being."
        " Friendly, helpful, focused on privacy and making the user feel comfortable"
        " I don't diagnose, just collect information to help you track your symptoms."
    ),
    allow_delegation=True
)

# Initial interview task
interview_task = Task(
    description=(
        "collect initial baseline health data from the user"
        " 1-10 scales where possible, in NL where not possible."
        " Goal is to collect data that can be input into a DB"
        " categories include general health, sleep, exercise, nutrition, mental health, medications, allergies, health conditions, family history, diet"
        " any specific symptoms or concerns that the patient wants to track."
    ),
    expected_output='a database of the user\'s health data',
    agent=initial_interviewer,
    output_file='new-db.csv'
)

# Daily follow-up interviews
write_task = Task(
    description=(
        "Complete a daily follow-up interview with the patient"
        " Check on if baseline information has changed, and update DB with new daily entry "
        " Ask follow-up questions where needed to get more detailed information"
        " enter information into DB in machine-readable format"
    ),
    expected_output='A daily entry in the patient\'s DB that can be references for trends and changes over time',
    agent=daily_interviewer,
    async_execution=False,
    output_file='new-entry.csv'  # Example of output customization
)

class InterviewState(Enum):
    WELCOME = auto()
    GENERAL_HEALTH = auto()
    SLEEP = auto()
    EXERCISE = auto()
    NUTRITION = auto()
    MENTAL_HEALTH = auto()
    MEDICATIONS = auto()
    ALLERGIES = auto()
    HEALTH_CONDITIONS = auto()
    FAMILY_HISTORY = auto()
    DIET = auto()
    END = auto()

user_states = {}

def get_user_state(user_id):
    return user_states.get(user_id, InterviewState.WELCOME)

def update_user_state(user_id, state):
    user_states[user_id] = state

def append_history(content, role):
    messages_list.append({"role": role, "content": content})
    return messages_list

def clear_history():
    messages_list.clear()
    return messages_list

async def process_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_state = get_user_state(user_id)

    if user_state == InterviewState.WELCOME:
        response = "Welcome to your health coach! Before we start, all information shared is strictly confidential."
        update_user_state(user_id, InterviewState.GENERAL_HEALTH)
    elif user_state == InterviewState.GENERAL_HEALTH:
        append_history(update.message.text, "user")
        response = "How have you been feeling overall?"
        update_user_state(user_id, InterviewState.END)  # Update accordingly
    else:
        response = "Thank you for sharing. Feel free to start over or ask another question."
        update_user_state(user_id, InterviewState.WELCOME)  # Reset to start

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def reset_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    clear_history()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Messages history cleaned")

def generate_gpt_response():
    completion = openai.ChatCompletion.create(model=openai_version, messages=messages_list)
    return completion.choices[0].message["content"]

if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_token).build()
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), process_text_message)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("reset", reset_history))
    application.run_polling()
