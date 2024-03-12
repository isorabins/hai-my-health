import openai
import os
import logging
from enum import Enum, auto
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
    CommandHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

telegram_token = os.environ["TELEGRAM_TOKEN"]
openai.api_key = os.environ["OPENAI_TOKEN"]
openai_version = os.environ["OPENAI_VERSION"]

messages_list = []

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
    # Add other states as needed
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
        # Determine next state based on response
        update_user_state(user_id, InterviewState.END)  # Update accordingly
    else:
        response = "Thank you for sharing. Feel free to start over or ask another question."
        update_user_state(user_id, InterviewState.WELCOME)  # Reset to start

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def reset_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    clear_history()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Messages history cleaned")
    return messages_list

def generate_gpt_response():
    completion = openai.ChatCompletion.create(model=openai_version, messages=messages_list)
    return completion.choices[0].message["content"]

if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_token).build()
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), process_text_message)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("reset", reset_history))
    application.run_polling()