# -*- coding: utf-8 -*-
# >>> Nitro Miner <<<

import httpx, random, string

from mod.ansi import ANSI



a = ANSI()






def _get_nitro_code(type: int = 1):
        if type == 1:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
            return code
        elif type == 2:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
            return code
        else:
            return None









class Nitro:
    def __init__(self):
        super(Nitro, self)
        self.valid_nitro = 0
        self.invalid_nitro = 0

    def _chct(self, title: str):
        pass




    def NitroMiner(self, proxy: any, code = _get_nitro_code()):
        try:
            url = httpx.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}", proxies=proxy, timeout=3)
            if url.status_code == 200:
                print(f"{a.White}[ {a.Green}+ {a.White}] {a.Green}Working Code {a.Purple}{code}{a.Reset}")
                open("./working_codes.txt", "w").close()
                f = open("./working_codes.txt", "a+")
                f.write(f"discord.gift/{code}\n")
                f.close()
            elif url.status_code == 404:
                print(f"{a.White}[ {a.Red}- {a.White}] {a.Red}Invalid Code {a.White}{code}")
            elif url.status_code == 429:
                print(f"{a.White}[ {a.Red}- {a.White}] {a.White}Proxy {a.White}{proxy}{a.White} is ratelimited! | Switching proxy")
                return False
            else:
                print(f"{a.White}[ {a.Red}! {a.White}] {a.White}Invalid Error! | Status code {a.White}{url.status_code}")
                return False
        except:
            print(f"{a.White}[ {a.Red}- {a.White}] {a.Blue}Failed connecting to proxy {a.White}{proxy}{a.White}")
            return False


