from instabot import Bot
import schedule
import time

bot = Bot()

username = "turgay.kr"
password = "a10163645826"
sevgilim = "kubraaormn"

bot.login(username=username, password=password)

def gunaydin():
    message = "Python instabot try.4-again"
    girlfriend = [sevgilim]

    bot.send_message(message, sevgilim)


schedule.every().day.at("10:00").do(gunaydin)

while True:
    schedule.run_pending()
    time.sleep(1)
