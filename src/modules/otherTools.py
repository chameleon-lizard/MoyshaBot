from src.modules.xlsxTools import getMessage

import requests as r
import wikipedia
import random

def agro(text):
    phrases = [ \
                f'Как говорил мой дед: "Любишь кататься - катись на хуй, {text}".',
                f"Да, я могу допускать ошибки в тексте. Но какие же они пиздатые, что так и ебут тебя в глаза, как сучку, {text}.", 
                f"Ноги есть, {text}? Тогда съебался нахуй.",
                f"Извини, но мама учила меня не разговаривать с таким говном, как {text}.",
                f"{text}, ты как муравей, несёшь всякую хуйню.", 
                f"{text}, ты всегда так глуп или сегодня особый случай?",
                f"Я видел людей, как {text}, но тогда мне надо было заплатить за билет в цирк.",
                f"{text}, кто поджёг запал на твоём тампоне?",
                f"{text}, тебе не хватает тампона во рту, потому что если собираешься вести себя, как пизда, то выгляди соотвествующе.",
                f"{text}, шокируй меня. Скажи что-нибудь умное.",
                f"{text}, не знаю, что делает тебя таким дебилом. Однако это точно работает.",
                f"Бог создал горы, Бог создал деревья, Бог создал {text}, но все мы совершаем ошибки.",
                f"{text}, клуб мазохизма на два этажа ниже..."
            ]
    return random.choice(phrases)

def textToEmoji(text):
    headers = {
        'authority': 'textgenerator.ru',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'origin': 'https://textgenerator.ru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://textgenerator.ru/font/emoji',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '_ym_uid=1624568435313291772; _ym_d=1624568435; _ym_isad=1',
        'dnt': '1',
        'sec-gpc': '1',
    }

    data = {
      "text": text
    }

    response = r.post("https://textgenerator.ru/font/emoji/ajax", headers=headers, data=data)
    return response.text

def markov(text, moysha):
    try:
        n = int(text[13:])
        if n not in range(1, 9):
            raise TypeError
        return f"> {text[13:].capitalize()}\n> {moysha.generate(n, window=n)}"
    except TypeError:
        return "Иди нахуй, дешёвка. Нормальное значение окна задай, потом выёбывайся."
    except:
        return f"> {text[13:].capitalize()}\n> {moysha.generate(4)}"

def roll(text):
    if len(text) == 5:
        return str(random.randint(0,10))
    else:
        fd = text[6:text.find("-")]
        sd = text[text.find("-")+1:]

        try:
            fd = int(fd)
            sd = int(sd)

            if (fd < sd):
                return str(random.randint(fd, sd))
            else:
                return "Хочешь наебать меня, дешёвка?"
        except:
            return "Хочешь наебать меня, дешёвка?"

def ahaha():
    if random.randint(0,100) < 10:
        return "Анафема."
    else:
        return "АХ" * random.randint(4,15)

def wikiBot(text):
    wikipedia.set_lang("ru")

    try:
        textNew = wikipedia.summary(text)
    except wikipedia.DisambiguationError as e:
        textNew = "Возможно, вы имели в виду: " + str(e.options)[2:-2].replace("'","")
    except wikipedia.exceptions.PageError as e:
        textNew = "По запросу "" + text + "" ничего не найдено."
    return textNew

def decodeFun(text):
    file = open("dict/sortWords.txt", "r")  
    lines = file.readlines()
    message = ""

    for i in range(len(text)):
        wordsLetter = [value for value in lines if value[0] == text[i].lower()]
        message += text[i] + " - " + wordsLetter[random.randint(0, len(wordsLetter)-1)]
    return message

def staticCMD(text, idS):
    answer = getMessage(text)
    if answer[0] != "None":
        if answer[2] == idS:
            return answer[0], answer[1]
        else:
            if answer[3] == True:
                return answer[0], answer[1]
            elif random.randint(0, 100) > 85:
                return answer[0], answer[1]
