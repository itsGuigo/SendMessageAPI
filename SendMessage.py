import requests
from urllib.parse import quote

PHONE_NUMBER = "XXXXXXXXXXXX"
CALLME_BOT_API_KEY = "8020982"

message = "Hello World"

try:
    requests.get(
        url=f'https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={quote(message)}&apikey={CALLME_BOT_API_KEY}'
    )

except Exception as e:
    print(f"{e}")