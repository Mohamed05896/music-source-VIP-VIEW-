from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/9681d7086cc9c32b85d5a.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/c1c0f856a869169722289.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VIP3V_bot")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VIP_3112")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5212007011").split()))


FAILED = "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bXVzaWN8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60"
, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bXVzaWN8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60"
