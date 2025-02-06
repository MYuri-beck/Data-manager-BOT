from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

token = os.getenv ("KEY_API")

class TelegramBot:
    def __init__(self):
        token = os.getenv ("KEY_API")
        self.url = f"https://api.telegram.org/bot{token}/"

    def start(self):
       update_id = None
       while True:
            update = self.get_message(update_id)
            if 'result' in update:
                messages = update['result']
                if messages:
                    for message in messages:
                        try:
                            update_id = message['update_id']
                            chat_id = message['message']['from']['id']
                            message_text = message["message"]["text"]
                            response_bot = self.generate_response(message_text)
                            self.send_response(chat_id, response_bot)
                        except:
                            pass
    
    def get_message(self, update_id):
        linkRequest = f"{self.url}getUpdates?timeout=1000" ##alterar valor do timout##
        if update_id:
            linkRequest = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"
        result = requests.get(linkRequest)
        return json.loads(result.content)
    
    def generate_response(self, message_text):
        if message_text in ["oi", "ola", "eae"]:
            return "cala a boca"
        else:
            return "Não entendi..."
    
    def send_response(self, chat_id, response):
        link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={response}"
        requests.get(link_to_send)
        return