# -*- coding: utf-8 -*-

import wrinter as wrinter
from gen_selenium import gen
from verify_mail import Verify
import os

try:
    import ctypes
    import time
    import string
    from colorama import Fore, Back, Style
    import datetime
    import sys
    import json
    import platform
    from pystyle import Colorate, Colors
    import time
    import typing
    import random
    from rich.console import Console
    import httpx
    from configparser import ConfigParser
    from faker import Faker
except:
    os.system("pip install -r requirements.bin")

# init(autoreset=True) pyStyle BUG

__info__ = {
    "appname": "DisGen",
    "version": "1.0.0",
    "logspath": "logs/logs.log",
    "proxyfile": "proxies.txt",
    "usernamesfile": "usernames.txt"
}


parser = ConfigParser()
parser.read("settings.cfg")

mailslurp_api_key = parser.get("emails", "mailslurp_api_key")

p = wrinter.wrint()

locales = ["AR_eg", "ar_JO", "FI_fi", "ja_JP", "hr_HR", "ru_RU"]

fake = Faker([random.choice(locales)])

class tools:

    def __init__(self):
        super(tools, self).__init__()

    @property
    def get_username(self) -> str:
        #req = httpx.get(url="https://api.namefake.com", timeout=1000)
        #json.loads(req.text)["name"]
        return str(fake.name())

    @property
    def get_password(self) -> str:
        __password = "".join(random.choices(string.ascii_letters, k=10) + random.choices(str(string.digits), k=4))
        return __password


    def logo(self) -> str:
        #https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Bloody&text=DISGEN
        return(Colorate.Vertical(Colors.purple_to_blue, r"""
                
                ▓█████▄  ██▓  ██████   ▄████ ▓█████  ███▄    █ 
                ▒██▀ ██▌▓██▒▒██    ▒  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
                ░██   █▌▒██▒░ ▓██▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
                ░▓█▄   ▌░██░  ▒   ██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
                ░▒████▓ ░██░▒██████▒▒░▒▓███▀▒░▒████▒▒██░   ▓██░
                ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
                ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
                ░ ░  ░  ▒ ░░  ░  ░  ░ ░   ░    ░      ░   ░ ░ 
                ░     ░        ░        ░    ░  ░         ░ 
                ░                                                    
                """,1))


    def machine(self):
        (p.ok(f"Your system architecture is compatible with {__info__['appname']}")) if (platform.architecture()[0]) == ("64bit") else p.warning(f"Your system architecture [ {platform.architecture()[0]} ] may cause errors. [Accepted]", return_only=True)
        (p.ok(f"Your operating system is compatible with {__info__['appname']} [{platform.system()}]")) if (platform.system()) == ("Windows") else (p.warning(f"Your operating system may cause errors! [{platform.system()}]", return_only=True))
        (p.info(f"You are using {__info__['appname']} app version : [ {__info__['version']} ]", return_only=True))
    
        
    def showmenu(self) -> str | None:
        menu1 = f"""
        ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░▒▓█ [      DISGEN      ] █▓▒░▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
         ┗ [ Option ║ Function ║ Estimated Daily Income ] ┑
        【 ➔ ║ 1.1 ║ ⋆ ║ Account Generator ║ ⋆ 『 $10 -> $250 』 】
    """

        print(Colorate.Vertical(Colors.red_to_blue, menu1, 3))

        action = input(Colorate.Vertical(Colors.green_to_blue, "┗", 3) + Style.RESET_ALL)
        return action
    
    @property
    def cls(self):
        try:
            os.system("cls") if os.name == "nt" else os.system("clear")
        except:
            p.warning("Unable to clear console")

ver = Verify(mailslurp_api_key)

if __name__ == "__main__":
    try:
        print(tools().logo())
        ctypes.windll.kernel32.SetConsoleTitleW(f'{__info__["appname"]} | {__info__["version"]}')
        tools().machine()
        if gen(mailslurp_api_key).install_solver() == True:
            tools().showmenu()
            gen(mailslurp_api_key).main(threads=1, email=f"{ver.CreateEmail()[0]}" + '@mailslurp.com', password=tools().get_password, username=tools().get_username, proxy=None, headless=False) #"91.246.195.196:6965"
        else:
            pass

    except KeyboardInterrupt:
        p.handle("Exiting")