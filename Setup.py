import os
import platform
import time
import requests

print("Installer v1.0")
time.sleep(3)
print("Installing libraries...")
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
print("All libraries were installed successfully.")

from colorama import Fore

try:
    os.mkdir("DATA")
except:
    pass

def download_files():
    urls = {
        "http://whz7qjw7.10001mb.com/main.py": "main.py",
        "http://whz7qjw7.10001mb.com/Login.py": "Login.py",
        "http://whz7qjw7.10001mb.com/errors.py": "errors.py",
        "http://whz7qjw7.10001mb.com/HELP.txt": "HELP.txt",
        "http://whz7qjw7.10001mb.com/Debug.py": "Debug.py",
        "http://whz7qjw7.10001mb.com/sticker01.webp": "DATA/sticker01.webp",
        "http://whz7qjw7.10001mb.com/sticker02.webp": "DATA/sticker02.webp"
    }
    for url, filename in urls.items():
        r = requests.get(url, allow_redirects=False)
        if r.status_code == 200:
            print(f"[{Fore.GREEN}{r.status_code}{Fore.RESET}] {Fore.WHITE}{r.url}{Fore.RESET} [{Fore.GREEN}{r.reason}{Fore.RESET}]")
            open(filename, "wb").write(r.content)
        elif r.status_code == 403:
            print(f"[{Fore.YELLOW}{r.status_code}{Fore.RESET}] {Fore.WHITE}{r.url}{Fore.RESET} [{Fore.YELLOW}{r.reason}{Fore.RESET}]")
            print("Please connect to a VPN.")
        else:
            print(f"[{Fore.RED}{r.status_code}{Fore.RESET}] {Fore.RED}{r.url}{Fore.RESET} [{Fore.RED}{r.reason}{Fore.RESET}]")
            print("Please tell the developer.")
            
print("Downloading files...")
download_files()
