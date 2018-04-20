from microsoftbotframework import ReplyToActivity
import json
import apiai
import pymorphy2
import re

# azure boot camp
CLIENT_ACCESS_TOKEN = '%%%%'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
ma = pymorphy2.MorphAnalyzer()


def echo_response(message):
    if message["type"] == "message":
        print(message)
        ReplyToActivity(fill=message,
                        text=qamaker(message["text"])).send()


def qamaker(message):
    # sent = bot.send_message(message.chat.id, "Shoot, cowboy")
    text = (str(message.replace("\\", " ")))
    text = text.lower()
    # deleting newlines and line-breaks
    text = re.sub('\-\s\r\n\s{1,}|\-\s\r\n|\r\n', '', text)
    # deleting symbols
    text = re.sub('[.,:;_%©?*,!@#$%^&()|\d]|[+=]|[[]|[]]|[/]|"|\s{2,}|-', ' ', text)
    text = " ".join(ma.parse(word)[0].normal_form for word in text.split())
    text = ' '.join(word for word in text.split() if len(word) > 1)
    # print(text)
    question = text
    request = ai.text_request()
    request.lang = 'ru'
    request.session_id = "%%%"
    request.query = question
    answer = json.loads(request.getresponse().read().decode('utf-8'))
    if answer:
        resp = answer['result']['fulfillment']['speech']
        return resp
    else:
        pass
