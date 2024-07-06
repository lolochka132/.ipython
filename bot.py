from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from test_parser import parse_hh
from .db import save_vacancies, get_analytics

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to HH Parser Bot! Send me a query to parse HH.ru.')

def parse(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    vacancies = parse_hh(query)
    save_vacancies(vacancies)
    total_vacancies = get_analytics()
    update.message.reply_text(f'Parsed {len(vacancies)} vacancies. Total vacancies in DB: {total_vacancies}')

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, parse))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()