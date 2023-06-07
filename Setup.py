import os
import platform
from time import sleep

print("installer v1.0")
sleep(3)
print("installing libraries...")
os.system("pip install colorama")
os.system("pip install cryptography")
os.system("pip install pyrogram")
os.system("pip install requests")
os.system("pip install TgCrypto")
os.system("pip install python-dotenv")

if platform.system() == "Windows":
    os.system("cls")
if platform.system() == "Linux":
    os.system("clear")

print("all libraries were installed successfully")

from colorama import Fore
import requests
import os

try:
    os.mkdir("DATA")
except:
    pass

print("downloading files...")

main = "http://whz7qjw7.10001mb.com/main.py"
login = "http://whz7qjw7.10001mb.com/Login.py"
errors = "http://whz7qjw7.10001mb.com/errors.py"
help = "http://whz7qjw7.10001mb.com/HELP.txt"
debug = "http://whz7qjw7.10001mb.com/Debug.py"
sticker01 = "http://whz7qjw7.10001mb.com/sticker01.webp"
sticker02 = "http://whz7qjw7.10001mb.com/sticker02.webp"

r1 = requests.get(main, allow_redirects=False)
r2 = requests.get(login, allow_redirects=False)
r3 = requests.get(errors, allow_redirects=False)
r4 = requests.get(help, allow_redirects=False)
r5 = requests.get(sticker01, allow_redirects=False)
r6 = requests.get(sticker02, allow_redirects=False)
r7 = requests.get(debug, allow_redirects=False)
request_lsit = [r1, r2, r3, r4, r5, r6, r7]
for r in request_lsit:
    if r.status_code == 200:
        print(
            f"[{Fore.GREEN}{r.status_code}{Fore.RESET}] {Fore.WHITE}{r.url}{Fore.RESET} [{Fore.GREEN}{r.reason}{Fore.RESET}]")
    elif r.status_code == 403:
        print(
            f"[{Fore.YELLOW}{r.status_code}{Fore.RESET}] {Fore.WHITE}{r.url}{Fore.RESET} [{Fore.YELLOW}{r.reason}{Fore.RESET}]")
        print("Please connect to a vpn")
    else:
        print(
            f"[{Fore.RED}{r.status_code}{Fore.RESET}] {Fore.RED}{r.url}{Fore.RESET} [{Fore.RED}{r.reason}{Fore.RESET}]")
        print("Please tel the developer!")

open("main.py", "wb").write(r1.content)
open("Login.py", "wb").write(r2.content)
open("errors.py", "wb").write(r3.content)
open("HELP.txt", "wb").write(r4.content)
open("DATA/sticker01.webp", "wb").write(r5.content)
open("DATA/sticker02.webp", "wb").write(r6.content)
open("Debug.py", "wb").write(r7.content)
