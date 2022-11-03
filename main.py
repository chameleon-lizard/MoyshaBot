from src.transcribe import transcribe
from src.converse import converse
from src.modules.markov import Markov
from dotenv import load_dotenv

import telebot
import os

class Bot:
    def __init__(self, TG_token, HF_token) -> None:
        self.bot = telebot.TeleBot(TG_token)
        self._hf_token = HF_token
        self._moysha = Markov(4)

        @self.bot.message_handler(content_types=["text"])
        def conversation(message):
            answer = converse(message, self._moysha)
            if isinstance(answer, str):
                if answer != "PhotoSent":
                    self.bot.send_message(message.chat.id, answer)
            if isinstance(answer, tuple) and len(answer) == 2:
                text, image = answer
                if text != "":
                    self.bot.send_message(message.chat.id, text)
                if image != "":
                    self.bot.send_photo(message.chat.id, open(f"./photos/{image}", "rb"))
                else:
                    self.bot.send_message(message.chat.id, text)
                    self.bot.send_photo(message.chat.id, open(f"./photos/{image}", "rb"))

        @self.bot.message_handler(content_types=["voice"])
        def voice_to_text(message):
            voice_id = message.voice.file_id
            voice_file = self.bot.get_file(voice_id)
            voice_bytes = self.bot.download_file(voice_file.file_path)

            self.bot.send_message(message.chat.id, transcribe(voice_bytes, self._hf_token))

    def run(self):
        self.bot.infinity_polling()

if __name__ == '__main__':
    load_dotenv()
    b = Bot(TG_token=os.getenv("TELEGRAM_TOKEN"), HF_token=os.getenv("HF_TOKEN"))
    b.run()