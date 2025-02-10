from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text('Hello! I am your bot. Use /help to see available commands.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help information when the command /help is issued."""
    help_text = """
Available commands:
/start - Start the bot
/help - Show this help message
/echo [message] - Echo back your message
"""
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def init_bot():
    """Initialize and configure the bot."""
    if not BOT_TOKEN:
        raise ValueError("No BOT_TOKEN provided in environment variables")
        
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    return application

if __name__ == '__main__':
    # If running directly, start the bot in polling mode
    bot = init_bot()
    bot.run_polling()
