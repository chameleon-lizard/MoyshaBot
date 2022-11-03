from src.modules.otherTools import decodeFun, markov, roll, ahaha, textToEmoji, agro, wikiBot, staticCMD
from src.modules.aboba import getYAML
from src.modules.zhirik import draw_text, draw_image
from src.modules.boyan import Boyan


import requests as r
import random


def converse(message, moysha):
    text = message.text.lower()
    if text == "да":
        return "Пизда"
    elif text == "нет":
        return "Пидора ответ"
    elif text == "скинь сиськи":
        return "(.Y.)"
    elif text == "бот, оцени":
        return "Оцениваю " + text[11:] + ", как " + str(random.randint(0,10)) + "/10"
    elif text == "мойша гпт":
        return "Не работает. Найдите мне норм вариант инференса не на моей малинке и я сделаю."
    elif text in {"баян?", "боян?", "бабаян?"}:
        return "Не работает. Добавить потом."
    elif text[:5] == "/roll":
        return roll(text)
    elif random.randint(0, 100) < 40 and "ахах" in text or "пхах" in text or "азаз" in text:
        return ahaha()
    elif text[:12] == "мойша марков":
        return markov(text, moysha)
    elif text[-1] == "?" and random.randint(0, 100) < 3:
        return f"> {text.capitalize()}\n> {moysha.generate(query=text[:-1])}"
    elif text[:9] == "расшифруй":
        return decodeFun(text[10:])
    elif text[:len("текст в эмодзи")] == "текст в эмодзи":
        return textToEmoji(text[len("текст в эмодзи")+1:])
    elif text[:14] == "бот, быкани на":
        return agro(text[15:])
    elif (text[:5] == "абоба"):
        try:
            return f"🅰🅱🅾🅱🅰: {getYAML(text[8:], text[6])}"
        except:
            return "Ошибка ввода для абобы"
    elif (text[:4] == "гпт3"): # GPT3
        return "Не работает. Найдите мне норм вариант инференса не на моей малинке и я сделаю."
    elif (text[:4] == "вики"): # Wiki
        return wikiBot(text[5:])
    if (text == "соя"):
        #soyjakMain(evnt, event)
        return "PhotoSent"
    elif (text == "жирик"):
        draw_text(text)
        return "PhotoSent"
    elif (text == "жирик фото"):
        #zhirikPhoto(evnt, event)
        return "PhotoSent"
    else: # Табличные команды
        return staticCMD(text, -1)
            
