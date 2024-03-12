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
    CallbackContext,
    ConversationHandler
)

# Set up logging to help with debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables for API keys
telegram_token = os.getenv("TELEGRAM_TOKEN")
openai.api_key = os.getenv("OPENAI_TOKEN")
openai_version = os.getenv("OPENAI_VERSION")

messages_list = []

# Enum for managing the conversation states
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

# Function to start the interview
def start_interview(update: Update, context: CallbackContext) -> int:
    logging.info("Starting the interview")
    update.message.reply_text("Welcome to Hai, your health coach! Your privacy is paramount to us.")
    return InterviewState.GENERAL_HEALTH

# Function to ask the general health question
def general_health_question(update: Update, context: CallbackContext) -> int:
    logging.info("Asking about general health")
    update.message.reply_text("How have you been feeling overall? It's all private.")
    return InterviewState.SLEEP

# Define additional question functions here...

# Function to conclude the interview
def end_interview(update: Update, context: CallbackContext) -> int:
    logging.info("Interview ended")
    update.message.reply_text("Congrats on taking the first step to better health! Looking forward to talking tomorrow!")
    return ConversationHandler.END

# Error handler function
def error_handler(update: object, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Main function where the bot is set up
if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_token).build()

    # Define the conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_interview)],
        states={
            InterviewState.GENERAL_HEALTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, general_health_question)],
            # Add other state handlers here...
        },
        fallbacks=[CommandHandler('cancel', end_interview)],
    )

    # Add the conversation handler to the application
    application.add_handler(conv_handler)

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling()
