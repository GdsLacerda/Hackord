# -*- coding: utf-8 -*-
# Hackord Setup

import os, uuid, time, datetime
import sys
import os, httpx, subprocess
import re, io
import zipfile
import platform




class ChromeDriver:
    def __init__(self) -> None:
        self.ing = None




    def _check_path(self,path):
        if not os.path.exists(path):
            os.makedirs(path)


    def _save(self,download_url, filepath):
        print("downloading", download_url, "...")
        response = httpx.get(download_url)
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(filepath)
        print(f"saved the driver to {filepath}/")


    def _download(self, pf: str):
        chromium_version = self._get_chrome_version(pf)
        base_url = 'https://chromedriver.storage.googleapis.com/'
        filepath = f'{os.getcwd()}'
        self._check_path(filepath)
        if pf == "linux":
            download_url = base_url+f'{chromium_version}/chromedriver_linux64.zip'
            self._save(download_url, filepath)
        elif pf == 'darwin':
            download_url = base_url+f'{chromium_version}/chromedriver_mac64.zip'
            self._save(download_url, filepath)
        elif pf == 'windows':
            download_url = base_url+f'{chromium_version}/chromedriver_win32.zip'
            self._save(download_url, filepath)


    def _get_chromium_version(self,release_string: str):
        version_number = re.search('\d+\.+\d+\.+\d+', release_string).group()
        print("Browser Version:", version_number)
        chromium_version = httpx.get(f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version_number}').text
        print("Chromium Version:", chromium_version)
        return chromium_version


    def _get_chrome_version(self,pf: str):
        if pf == 'linux':
            command = "google-chrome --version"
            release_string = subprocess.check_output(command.split(" ")).decode('utf-8')
            version_number = self._get_chromium_version(release_string)
            return version_number
        elif pf == 'darwin':
            command = "grep -a1 CFBundleShortVersionString /Applications/Google\ Chrome.app/Contents/Info.plist | tail -1"
            release_string = subprocess.check_output(command, shell=True).decode('utf-8')
            version_number = self._get_chromium_version(release_string)
            return version_number
        elif pf == 'windows':
            command = 'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            release_string = [line.decode('utf-8') for line in process.stdout][2]
            version_number = self._get_chromium_version(release_string)
            return version_number





class ANSI:
    def __init__(self) -> None:
        super(ANSI, self).__init__()
        # Reset
        self.Reset='\033[0m'       # Text Reset

        # Regular Colors
        self.Black='\033[0;30m'        # Black
        self.Red='\033[0;31m'          # Red
        self.Green='\033[0;32m'        # Green
        self.Yellow='\033[0;33m'       # Yellow
        self.Blue='\033[0;34m'         # Blue
        self.Purple='\033[0;35m'       # Purple
        self.Cyan='\033[0;36m'         # Cyan
        self.White='\033[0;37m'        # White  


class Setup:
    def __init__(self) -> None:
        super(Setup, self)
        self.datafolder = os.path.join(os.getcwd(), "data")
    
    @property
    def runwarn(self):
        os.mkdir("logs")
        open("logs/hackord.log", "w").close()
        open("logs/webdriver.log", "w").close()
        print("Additional files not found.")
        print("Attempting to get additial files")
        print("Please be patient")
        print("Do not close this file")
        print(f"Setup running on PID: [ {os.getpid()} ]")
        
    @property
    def create_config_json(self):
        print("Creating JSON config with default settings")
        print("Please wait while we are taking an action")
        print(f"Work ID: [ {uuid.uuid4()} ]")
        configjson = open("data/config.json", "w")
        config = """
{
    "$README": [
        "Need help? | Join our Discord Server! - https://discord.gg/KCqrbVgSBF",
        "Hackord on Github: https://github.com/WieszakWare/Hackord"
    ],

    
    "Chromedriver": {
        "$README": [
            "INFO | Only free captcha solver need chromedriver",
            "1. Download Chromedriver for your operating system from https://chromedriver.chromium.org/downloads"],
        "chromedriver-path": "chromedriver.exe"
    },

    "Logs": {
        "webdriver-log": "./logs/webdriver.log",
        "hackord-log": "./logs/hackord.log"
    },

    "Tokens": {
        "$README": "Config Tokens",
        "tokens-file": "./data/tokens.txt"
    },

    "Proxies": {
        "$README": "Proxy Settings | Allowed proxy format: [ username:password@host:port ]",
        "type": "http",
        "proxy_file": "data/proxies.txt"
    },

    "Token-Generator": {
        "invite_code": "",
        "check-after-generating": true,
        "Confirm_Email": {
            "": ""
        }
    },

    "$README_Request": "Request settings will be deleted in next hackord version!",
    "Request": {
        "$README": "Set timeout / Edit headers | Experimental",
        "timeout": 20,

        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "referer": "https://discord.com/channels/@me",
        "content-type": "application/json",
        "accept": "*/*",
        "accept-language": "en-US",
        "connection": "keep-alive",
        "DNT": "1",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "TE": "Trailers"
    },

    "Rate_Limit": {
        "ratelimit_delay": "5"
    },

    "Captcha": {
        "$README": ["Captcha_Solver_Type [ 2captcha.com / hcaptcha_ai ] | Hcaptcha AI Requires chromedriver https://chromedriver.chromium.org/downloads"], 

        "Captcha_Solver_Type": "hcaptcha_ai",

        "wait_for_solved_captcha": "8",

        "2captcha": {
            
            "captcha_api_key": "PUT YOUR 2CAPTCHA API KEY HERE",
            "captcha_get_url": "http://2captcha.com/res.php",
            "captcha_submit_url": "http://2captcha.com/in.php",
            "discord_hcaptcha_sitekey": "4c672d35-0701-42b2-88c3-78380b0db560",
            "discord_captcha_referer": "https://discord.com/channels/@me"
        },
        "hcaptcha_ai": {
            "solver-retries": "4",
            "solver-host": "discord.com",
            "solver-sitekey": "4c672d35-0701-42b2-88c3-78380b0db560"
        }
    }
}
"""
        
        configjson.write(config)
        configjson.close()
        print("Successfully written [ config.json ] file!")
        
        
    @property
    def create_dirs(self):
        
        print(f"Handler Process UUID: [ {uuid.uuid4()} ]")
        
        print("Creating [ data ] folder.")

        os.mkdir("data")
            
        print("Folders created")
        
        print("Attempting to create files")
        
        print("Attempting to create file [ data/proxies.txt ]")
        
        try:
            print(f"File [ data/proxies.txt ] has been created in [ {os.getcwd()}/data/proxies.txt ] | Fullpath: [ {os.path.join(os.getcwd(), 'data', 'proxies.txt')} ]")
            with open('data/proxies.txt', 'w') as f:
                f.write('')
                f.close()
        except Exception as exc:
            print(f"Unable to create file: [ data/proxies.txt ] | Exception : [ {exc} ]")
            
        print("Attempting to create file [ data/proxies.txt ]")
            
            
        try:
            print(f"File [ data/tokens.txt ] has been created in [ {os.getcwd()}/data/proxies.txt ] | Fullpath: [ {os.path.join(os.getcwd(), 'data', 'tokens.txt')} ]")
            with open('data/tokens.txt', 'w') as f:
                f.write('')
                f.close()
        except Exception as exc:
            print(f"Unable to create file: [ data/tokens.txt ] | Exception : [ {exc} ]")
            
        print("Attempting to create file [ data/tokens.txt ]")


        try:
            print(f"File [ data/confirmation_emails.txt ] has been created in [ {os.getcwd()}/data/ ] | Fullpath: [ {os.path.join(os.getcwd(), 'data', 'input', 'tokens.txt')} ]")
            with open('data/confirmation_emails.txt', 'w') as f:
                f.write('')
                f.close()
        except Exception as exc:
            print(f"Unable to create file: [ data/confirmation_emails.txt ] | Exception : [ {exc} ]")
            


            
    def setuplogo(self):
        return("""
        
██   ██  █████   ██████ ██   ██  ██████  ██████  ██████  
██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██   ██ 
███████ ███████ ██      █████   ██    ██ ██████  ██   ██ 
██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██   ██ 
██   ██ ██   ██  ██████ ██   ██  ██████  ██   ██ ██████  
                                                         
                                                         
    ███████ ███████ ████████ ██    ██ ██████             
    ██      ██         ██    ██    ██ ██   ██            
    ███████ █████      ██    ██    ██ ██████             
         ██ ██         ██    ██    ██ ██                 
    ███████ ███████    ██     ██████  ██                  
        """)

    
    @property
    def download_chromedriver(self):
        ch = ChromeDriver()
        ch._download(platform.system().lower())

        
    @property
    def run(self):
        print(ANSI().Blue + self.setuplogo() + ANSI().Reset)
        start_setup = time.time()

        print(f"{ANSI().Red}[{ANSI().Reset} {ANSI().Yellow}DISCLAIMER{ANSI().Reset} {ANSI().Red}]{ANSI().Reset}{ANSI().Yellow}If operation was not successful, run the file as administrator{ANSI().Reset}")
        print("[ WORKER ] We need to create and download files")
        print("[ WORKER ] It may take a few minutes")
        print(f"Welcome {os.getlogin()}, please wait while we are taking an action.")
        self.runwarn
        self.create_dirs
        self.create_config_json
        print(f"[ WORKER ] Done")
        print(f"[ LOADER ] Loading")
        print(f"[ ATTEMPT ] We need to reload Hackord")
        print(f"[ INFO ] Attempting to reload Hackord")
        print(f"[ HC LAUNCHER ] Process ID: [ {uuid.uuid4()} ]")
        print("[ HANDLE SCRIPT ] Relaunching")

        end_setup = time.time()

        print(f"[ CLOSE ] Done in ( {end_setup-start_setup}s )")

        try:
            print(f"[ {os.getlogin()} ] Restart EXE")
            os.execl(sys.executable, sys.executable, *sys.argv)
        except Exception as e:
            print("[ ERROR ] There was an error")
            print(F"[ TRACE ] Setup Error: [ PID: [ {os.getpid()} ] | TRACE: [ {Exception} ] | TIME: {datetime.datetime.now()}]")
            print("[ RESTART ERROR ] Due to setup error you need to manually restart HackordV2 APP")
            time.sleep(6)

        

