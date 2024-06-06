import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Get TOKEN
TOKEN = 'YOUR_TOKEN'
GROUP_CHAT_ID = 'ID_CHAT'  

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Xin chào! Bot đã khởi động.')

def send_log_file(bot: Bot):
    file_path = r'C:\Program Files\log.txt'
    
    try:
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=GROUP_CHAT_ID, document=file)
    except FileNotFoundError:
        logger.error('Không tìm thấy file tại đường dẫn này.')
    except Exception as e:
        logger.error(f'Đã xảy ra lỗi: {e}')

def main():
    updater = Updater(TOKEN)
    bot = Bot(TOKEN)

    # Send file log.txt 
    send_log_file(bot)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
