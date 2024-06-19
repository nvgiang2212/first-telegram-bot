# Hi, my name is Gary
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! This is your bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help!')

if __name__ == '__main__':
    application = ApplicationBuilder().token('YOUR_TOKEN_HERE').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()
