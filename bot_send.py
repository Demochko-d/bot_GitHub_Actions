import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
THREAD_ID = os.environ.get("THREAD_ID")

text = "Тестовое сообщение раз в час"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": text,
}

if THREAD_ID:
    data["message_thread_id"] = THREAD_ID

response = requests.post(url, data=data, timeout=10)
response.raise_for_status()

print(response.json())