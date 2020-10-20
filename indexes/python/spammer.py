import requests, threading, colorama, os
from colorama import Fore, Style, init

colorama.init()

def sendtowebhook(webhook, message, username):
    data = {
        'content': message,
        'username': username
    }
    try:
        while True:
            requests.post(webhook, data=data)
    except KeyboardInterrupt:
        exit()

def webhook():
    os.system('mode con: cols=150 lines=20')
    os.system("title Zerp / Webhook Spammer")
    webhook = input( Fore.MAGENTA + "> " + Fore.RED + "Discord Webhook: ")
    message = input( Fore.MAGENTA + "> " + Fore.BLUE + "Webhook Message: ")
    print("\n\n" + Fore.YELLOW + "Success " + Fore.BLUE + "Closing This Stops The Spamming!!!!!\n")
    for x in range(99999999999):
        try:
            target=sendtowebhook(webhook, message, "Zerp / SelfBot")
        except Exception as e:
            print(Fore.MAGENTA + "> " + Fore.RED + "Webhook Not Sent" + Fore.YELLOW + "!")


webhook()