import os

API_ID    = os.environ.get("API_ID", 23476439)
API_HASH  = os.environ.get("API_HASH", "1626e884119a29dbccbb78e39b48128f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7407369394:AAHn3DSq_-1kK8ov1zxByeJRhLGUr1zCzdE") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
