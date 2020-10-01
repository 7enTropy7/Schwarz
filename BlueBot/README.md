[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Divyani-blue.svg)](https://www.linkedin.com/in/divyani-panda-5a8345194/) 
[![GitHub followers](https://img.shields.io/github/followers/7divs7?label=Follow&style=social)](https://github.com/7divs7?tab=followers) 
[![GitHub stars](https://img.shields.io/github/stars/7divs7/BlueBot.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/7divs7/BlueBot/stargazers/)

# BlueBot
A smart Telegram Bot that'll give you company during quarantine :P


# Instructions
```bash
$ python3 BlueBot/bot.py
```

Start ngrok to set up WebHook in order to receive a simple event-notification via HTTP POST
```bash
$ ./ngrok http 8080
```

Use the URL for setting up WebHook as shown below
![](images/ngrok_status.png)

Set up WebHook and check if it was successful
 https://api.telegram.org/bot1{your_bot_token}/setWebhook?url={ngrok_url}
 https://api.telegram.org/bot{your_bot_token}/getWebhookInfo

Now you're good to go!

# Output
![](images/output.png)

## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/divyani-panda-5a8345194/)
* [*Divyani Panda*](https://github.com/7divs7)
