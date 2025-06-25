from dotenv import load_dotenv
import os

### ПОДКАЧКА ДАННЫХ ИЗ .ENV ###

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
