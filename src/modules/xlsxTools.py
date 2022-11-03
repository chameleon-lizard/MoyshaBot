import pandas as pd
import random

# Упаковываем сообщение
def packMessage(row):
	text = row["Message"]
	att = row["Attachment"]
	Id = row["Id"]
	alwAns = row["Always answer"]
	message = []
	if text != "Null": # Собираем отправляемый текст
		if row["Random answer"] == False: # Проверяем на то должен ли быть случайный ответ (случайный текст)
			message.append(text.replace("\\n","\n"))
		else:
			text = text.split(';')
			k = random.randint(1, len(text)) - 1
			message.append(text[k])
	else:
		message.append('')
	if att != "Null": # Собираем отправляемые приложения (фото, видио, аудио, документы)
		message.append(att)
	else:
		message.append('')
	if  Id != "Null": # Собираем айди к которому привязана команда (то есть, чтобы реагировало только на 1 человека)
		message.append(-1)
	else:
		message.append('')
	message.append(alwAns) # Узнаём всегда ли бот должен реагировать на эту команду
	return message

# Получаем ответ на команду
def getMessage(text):
	df = pd.read_excel("./commands.xlsx")
	for i in range(len(df["Command"])):
		cmds = str(df["Command"][i]).split(', ')
		for cmd in cmds:
			if ((text == cmd) and (df["Fully include"][i] == True)) or ((cmd in text.replace(',','').split(' ')) and (df["Fully include"][i] == False)): # Нашли команду
				row = df.iloc[i]
				message = packMessage(row)
				return message
	return ["None"]
