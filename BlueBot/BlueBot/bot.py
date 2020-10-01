import re
import bs4
import requests  
from bottle import Bottle, response, request as bottle_request



class UserBot:  
    BOT_URL = None

    def get_chat_id(self, data):
        #extract chat id from telegram request.
        chat_id = data['message']['chat']['id']
        return chat_id

    def get_message(self, data):
        #extract message id from telegram request.
        message_text = data['message']['text']
        return message_text

    def send_message(self, prepared_data):
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)


class TelegramBot(UserBot, Bottle):  
    BOT_URL = 'https://api.telegram.org/bot{your_bot_token}/'

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")

    def change_text_message(self, text):
        #generate response 
        params = {"ENTRY": text}
        target_url = "http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi"
        resp = requests.post(target_url, data=params)
        soup_input = resp.text
        chatbot_output = (soup_input.split('<!-- Begin Response !--> <!-- Country:   -->'))[1].split('<!-- End Response !-->')[0]
        rep1=chatbot_output.split(' ')
        for n, i in enumerate(rep1):
            if i == "Elbot":
                rep1[n] = "BlueBot"
            if i == "Elbot.":
                rep1[n] = "BlueBot."
        new = ""
        for x in rep1: 
            new += x + " "
        chatbot_output = new
        return chatbot_output

    def prepare_data_for_answer(self, data):
        message = self.get_message(data)
        answer = self.change_text_message(message)
        chat_id = self.get_chat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }

        return json_data

    def post_handler(self):
        data = bottle_request.json
        answer_data = self.prepare_data_for_answer(data)
        self.send_message(answer_data)

        return response


if __name__ == '__main__':  
    app = TelegramBot()
    app.run(host='localhost', port=8080)
