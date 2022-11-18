# -*- coding: utf-8 -*-

import httpx, re, random, binascii, os



class Cloudfare:
    @staticmethod
    def Get_CFParams(session: httpx.Client):
        html = session.get('https://discord.com').text
        r = str(re.findall(r"r:'[^']*'", html)[0]).replace("r:'", "").replace("'", "")
        m = str(re.findall(r"m:'[^']*'", html)[0]).replace("m:'", "").replace("'", "")

        return [r, m]

    @staticmethod
    def Get_CfBm(session: httpx.Client, r: str, m: str) -> str:
        payload = {
            "m": m,  \
            "results": [
                str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                str(binascii.b2a_hex(os.urandom(16)).decode('utf-8'))
            ],
            "timing": random.randint(40, 120), 
            "fp": {
                "id": 3,
                "e": {
                    "r": [
                        1920,  # Height
                        1080   # Width
                    ],
                    "ar": [
                        1040,  # availHeight
                        1920   # availWidth
                    ],
                    "pr": 1,      # Pixel Ratio
                    "cd": 24,     # Color Depth
                    "wb": False,  # Web-driver
                    "wp": False,  # PhantomCall
                    "wn": False,  # NightMare
                    "ch": True,   # Chrome
                    "ws": False,  # Selenium
                    "wd": False   # domAutomation
                }
            }
        }

        return session.post(f'https://discord.com/cdn-cgi/bm/cv/result?req_id={r}', json=payload).cookies['__cf_bm']