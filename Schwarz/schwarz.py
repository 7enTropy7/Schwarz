import re
import bs4
import requests

def chatbot(input_text):
    params = {"ENTRY": input_text}
    target_url = "http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi"
    resp = requests.post(target_url, data=params)
    soup_input = resp.text
    chatbot_output = (soup_input.split('<!-- Begin Response !--> <!-- Country:   -->'))[1].split('<!-- End Response !-->')[0]
    return chatbot_output