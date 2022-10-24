# -*- coding: utf-8 -*-
import os
import re
import sys
import ctypes
import random
import typing
import json
import platform
import datetime
import time

from modules._solutions.yolo import Prefix

try:
    import mailslurp_client
    #print(f"[ IMPORT ] Import Successfull {mailslurp_client.__loader__}, {mailslurp_client.__package__}, {mailslurp_client.__file__}")
except ImportError:
    print(F"[ ERROR ] Unable to import module MailSlurp Client")
try:
    import configparser
    #print(f"[ IMPORT ] Import Successfull {configparser.__loader__}")
except ImportError:
    print(F"[ ERROR ] Unable to import module ConfigParser")
try:
    import faker
    #print(f"[ IMPORT ] Import Successfull {faker.__loader__}")
except ImportError:
    print(F"[ ERROR ] Unable to import module faker")

import modules as cap
import modules.exceptions

    
try:
    import undetected-chromedriver as uc
    from selenium.common.exceptions import (
        ElementClickInterceptedException,
        ElementNotInteractableException
    )
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import string
    import shutil
    from pystyle import Colorate, Colors
except ImportError:
    os.system("pip install -r requirements.bin")


__info__ = {
    "appname": "Hackord",
    "version": "v1",
    "logspath": "logs/logs.log",
    "proxyfile": "proxies.txt",
    "tokensfile": "output/tokens.txt",
    "jaccfile": "output/accounts.json",
    "authorization-page": lambda username, password, ip: f"https://wieszakware.pythonanywhere.com/api/experimental/ip-authorization/add?username={username}&password={password}&ip={ip}",
    "lastupdate": "08.10.2022" 
}



#----------------------------------START WRINT FUNCTION----------------------------------

reset_ansi = "\x1b[0m"


class wrint():

    def __init__(self):
        super(wrint, self).__init__()
        
    

    def aprint(self, text: str = None, t: float = 0.01) -> None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(t)
        print("\n")
    
    def session(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SESSION ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_blue, f"[ SESSION ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_blue, f"[ SESSION ] >" + " " + f"{text}",1) + reset_ansi


    def token(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            pass
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_green, f"[ TOKEN ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_green, f"[ TOKEN ] >" + " " + f"{text}",1) + reset_ansi


    def solver(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SOLVER ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_purple, f"[ SOLVER ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_purple, f"[ SOLVER ] >" + " " + f"{text}",1) + reset_ansi


    def handle(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ HANDLE ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_green, f"[ HANDLE ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_green, f"[ HANDLE ] >" + " " + f"{text}",1) + reset_ansi


    def info(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ INFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_blue, f"[ INFO ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_blue, f"[ INFO ] >" + " " + f"{text}",1) + reset_ansi


    def warning(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ WARNING ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.yellow_to_green, f"[ WARNING ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.yellow_to_green, f"[ WARNING ] >" + " " + f"{text}",1) + reset_ansi


    def debug(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ DEBUG ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ DEBUG ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ DEBUG ] >" + " " + f"{text}",1) + reset_ansi


    def critical(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.yellow_to_red, f"[ CRITICAL ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.yellow_to_red, f"[ CRITICAL ] >" + " " + f"{text}",1) + reset_ansi


    def error(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ ERROR ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_white, f"[ ERROR ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_white, f"[ ERROR ] >" + " " + f"{text}",1) + reset_ansi


    def ok(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ OK ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_blue, f"[ OK ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_blue, f"[ OK ] >" + " " + f"{text}",1) + reset_ansi

    
    def success(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SUCCESS ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ SUCCESS ] >" + " " + f"{text}",1) + reset_ansi)
        return reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ SUCCESS ] >" + " " + f"{text}",1) + reset_ansi

p = wrint()

#----------------------------------END WRINT FUNCTION----------------------------------


parser = configparser.ConfigParser()
parser.read("settings.cfg")

mailslurp_api_key = parser.get("emails", "mailslurp_api_key")
use_proxy_boolean = parser.getboolean("proxy", "use_proxy")


locales = ["en_GB"]

fake = faker.Faker([random.choice(locales)])

class tools:

    def __init__(self):
        super(tools, self).__init__()
        self.print_center = lambda text: print(text.center(shutil.get_terminal_size().columns))


    def get_username(self) -> str:
        #req = httpx.get(url="https://api.namefake.com", timeout=1000)
        #json.loads(req.text)["name"]
        return str(fake.name())


    def get_password(self) -> str:
        __password = "".join(random.choices(string.ascii_letters, k=10) + random.choices(str(string.digits), k=4))
        return __password


    def logo(self, username: str = os.getlogin()) -> str:
        #http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=Hackord
        print(Colorate.Horizontal(Colors.blue_to_purple, Fr"""
                        ██   ██  █████   ██████ ██   ██  ██████  ██████  ██████  
                        ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██   ██ 
                        ███████ ███████ ██      █████   ██    ██ ██████  ██   ██ 
                        ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██   ██ 
                        ██   ██ ██   ██  ██████ ██   ██  ██████  ██   ██ ██████  
                                                                                                    
                          Welcome {username} thanks for using Hackord {__info__['version']}! 
                                              
""",1))


    def machine(self):
        p.info(f"Using Python Version: [ {platform.python_version()} ]")
        p.ok(f"Your system architecture is compatible with {__info__['appname']}") if (platform.architecture()[0]) == ("64bit") else p.warning(f"Your system architecture [ {platform.architecture()[0]} ] may cause errors.")
        p.ok(f"Your operating system is compatible with {__info__['appname']} [ {platform.system()} ]") if (platform.system()) == ("Windows") else (p.warning(f"Your operating system may cause errors! [ {platform.system()} ]"))
        p.info(f"You are using {__info__['appname']} {__info__['version']}")
    
        
    def showmenu(self):
        menu1 = f"""
                        ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░▒▓█ [      HACKORD      ] █▓▒░▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        ┗ [ Option ║ Function ║ Estimated Daily Income ] ┑
                        【 ➔ ║ 1 ║ ⋆ ║ Account Generator ║ ⋆ 『 $- 』 】
                        
                        ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░▒▓█ [      SETTINGS      ] █▓▒░▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        ┗ [ Option ║ Function ║ Description ] ┑
                        【 ➔ ║ s1 ║ ⋆ ║ Reload Proxy File ║ ⋆ 『 $- 』 】
    """

        print(Colorate.Horizontal(Colors.red_to_purple, menu1, 2, 1))

    
    def clear(self):
        try:
            os.system("cls") if os.name == "nt" else os.system("clear")
        except:
            p.warning("Unable to clear console")




proxylist = set()


#Load Function
def pload():
    with open(file=__info__["proxyfile"], mode="r+") as rcp:
        rcpreadlines = rcp.readlines()
        for line in rcpreadlines:
            proxylist.add(line.replace("\n", ""))
        rcp.close()

#Count function
def pcount():
    return len(list(proxylist))

# return random proxy



# Load Proxies
pload()








class Verify:
    def __init__(self, api_key: str) -> None:
        super(Verify, self).__init__()
        self.configuration = mailslurp_client.Configuration()
        self.configuration.api_key['x-api-key'] = f"{api_key}"



    def CreateEmail(self):
        # Attemting to create mailbox
        try:
            api_client = mailslurp_client.ApiClient(self.configuration)

            # create an inbox using the inbox controller
            api_instance: mailslurp_client.InboxControllerApi = mailslurp_client.InboxControllerApi(api_client)
            inbox = api_instance.create_inbox()
            # check the id and email_address of the inbox
            if len(inbox.id) > 0:
                return [str(inbox.id), str(inbox.email_address)]
            else:
                p.warning("Unable to create mailbox")
                return "ERROR"
        except Exception as e:
            
            p.error("Monthly inbox limit reached! | Try to use different mailslurp account")
            p.handle("Insert new mailslurp API_KEY in settings.cfg")
            p.handle("Due to exception it's unable to generate discord token.")
            raise e
            time.sleep(100)
            sys.exit()




    def ReceiveEmail(self, mailbox_id: any):
        api_client = mailslurp_client.ApiClient(self.configuration)
        # create two inboxes for testing
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox = inbox_controller.get_inbox(mailbox_id)

        # receive email for inbox.id
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email1 = waitfor_controller.wait_for_latest_email(inbox_id=inbox.id, timeout=10000, unread_only=True)

        #body = re.sub(r'<.*?>', '', str(email.body))
        while True:
            #p.handle(f"Arrived Email: [ {email1.subject} ]")

            if str(email1.subject) == "Verify Email Address for Discord":
                try:
                    links1 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email1.body)
                    #p.info(f"Successfully got links [ {links1} ]")
                    #p.debug(f"Found [{len(links1)}] links in email")

                    discord_links_1 = list()

                    for l1 in links1:
                        if str(l1).startswith("https://click.discord.com"):
                            discord_links_1.append(str(l1))

                    #p.info(f"Links: {discord_links_1}")
                    return discord_links_1[1]
                except Exception as e:
                    print(e)
                    break

            else:
                #p.debug("Waiting for another verification mail")
                inbox_controller2 = mailslurp_client.InboxControllerApi(api_client)
                inbox2 = inbox_controller2.get_inbox(mailbox_id)

                waitfor_controller2 = mailslurp_client.WaitForControllerApi(api_client)
                email2 = waitfor_controller2.wait_for_latest_email(inbox_id=inbox2.id, timeout=10000, unread_only=True)
                try:
                    links2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email2.body)
                    #p.info(f"Successfully got links [ {links2} ]")
                    #p.debug(f"Found [{len(links2)}] links in email")
                    discord_links_2 = list()
                    for l2 in links2:
                        if str(l2).startswith("https://click.discord.com"):
                            discord_links_2.append(str(l2))
                    #p.info(f"Links: {discord_links_2}")
                    return discord_links_2[1]
                except Exception as e:
                    print(e)



ver = Verify(mailslurp_api_key)




# class Generator
class gen:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.solved = 0
        self.generated_accounts = 0

    
    # Solver Solve
    def hit_challenge(self, driver, challenger: cap.HolyChallenger, retries: int = 10) -> typing.Optional[str]:
        if challenger.utils.face_the_checkbox(driver):
            challenger.anti_checkbox(driver)

        if res := challenger.utils.get_hcaptcha_response(driver):
                p.info(f"HCaptcha Response [ {res} ]")
                return res

        for _ in range(retries):
            try:
                if (resp := challenger.anti_hcaptcha(driver)) is None:
                    continue
                if resp == challenger.CHALLENGE_SUCCESS:
                    return challenger.utils.get_hcaptcha_response(driver)
            except modules.exceptions.ChallengePassed:
                return challenger.utils.get_hcaptcha_response(driver)
            challenger.utils.refresh(driver)
            time.sleep(0.01)




    def main(self, threads: int, email: str, password: str, username: str, proxy: any = None, headless: bool = False):
            cap.install(Prefix.YOLOv6n)
            

            # New Challenger
            try:
                challenger = cap.new_challenger(screenshot=False, debug=False, lang="en", onnx_prefix=Prefix.YOLOv6n)
                p.session("New Challanger Started")
            except Exception as e:
                p.error(f"Unable to start challanger | Exception: [ {e} ]")
                time.sleep(10)
                sys.exit()

            # Replace selenium.webdriver.Chrome with driver
            try:
                driver = cap.get_challenge_ctx(headless=headless, proxy = proxy, lang="en")
                p.session("Challange Context ( STATUS: CONTINUE )")
            except:
                p.critical(f"Unable to get challange context. | Exception: [ {e} ]")
                time.sleep(10)
                sys.exit()
                



            try:
                driver.get("http://discord.com/register")
                p.handle(f"Driver: [ {driver.name} ] started successfully.")
            except Exception as e:
                p.error(f"Unable to start webdriver. | Exception: [ {e} ]")
                p.handle("Exception Handled")
                time.sleep(10)
                sys.exit()
  

            try:
                # XXX: Insert Email
                WebDriverWait(driver, 15, ignored_exceptions=(ElementNotInteractableException,)).until(
                    EC.presence_of_element_located((By.NAME, "email"))
                ).send_keys(email)
            except:
                pass
            
            try:
                # XXX: Insert Username
                WebDriverWait(driver, 15, ignored_exceptions=(ElementNotInteractableException,)).until(
                    EC.presence_of_element_located((By.NAME, "username"))
                ).send_keys(username)
            except:
                pass
               
            
            try:
                # XXX: Insert Password
                WebDriverWait(driver, 15, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                ).send_keys(password)
            except:
                pass

            actions = ActionChains(driver)
            
            # BUG: TYPE: Discord DESC: Locating to the first date input then the discord will navigate the focuse to the next input
            driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click() 
            actions.send_keys(str(random.randint(1,12))) # Submitting the month
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1,28))) # Submitting the day
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1990,2001))) # Submitting the year
            actions.send_keys(Keys.ENTER)
            actions.perform() # All the actions are pending and needs to perform all at once 



            # XXX Agree to terms and conditions DISCORD TOS
            try: 
                checkbox_cssselector = (
                    "#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div > div > form > div > div > div.flex-2S1XBF.flex-3BkGQD.horizontal-112GEH.horizontal-1Piu5-.flex-3BkGQD.directionRow-2Iu2A9.justifyStart-2Mwniq.alignCenter-14kD11.noWrap-hBpHBz.marginTop20-2T8ZJx > label > input"
                ) # Discord ToS Checkbox CSS_SELECTOR
                checkbox_full_xpath = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/label/input" # RECOMMENDED: Full XPATH
                checkbox_xpath = '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/label/input' # Discord ToS Checkbox xpath

                # OLD: checkbox = driver.find_element(By.XPATH, checkbox_full_xpath) # Find Checkbox Element
                # OLD: checkbox.click() # ACTION: Click checkbox - Agree to discord terms and conditions

                WebDriverWait(driver, 15, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.presence_of_element_located((By.XPATH, checkbox_full_xpath))
                ).click()
            except Exception as e:
                p.error(f"Unable to accept Discord TOS")
                #driver.quit()


            # XXX Click Signup Button
            try:
                # XXX: Insert Password
                elements = driver.find_elements(By.TAG_NAME, 'button')
                # OLD : p.debug(f"Signup button Located: [ {elements[0].text} ]")
                # OLD : print(elements[0].text)
                elements[0].click()
            except:
                p.error("Unable to click signup button")
                driver.quit()

            p.handle("Creating Account")

            p.solver("Solving Captcha")


            start = time.time()

            try:
                self.hit_challenge(driver, challenger=challenger, retries=10)
            except:
                pass

            end = time.time()

            self.solved += 1


            p.solver(f"Captcha Solved in [ {end - start} ] seconds.")

            class SDEV:
                def __init__(self) -> None:
                    super(SDEV, self)

                def switch_tab(self,  driver: uc.Chrome, tab: int = 0):
                    driver.window_handles[tab]

                def changeurl(self, url: str):
                    driver.get(url)

            p.session(f"Solved Captchas in this session: [ {self.solved} ]")

            vy = Verify(self.api_key)

            rm = vy.ReceiveEmail(email[:-14])
            # print(rm)

            token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"') # Get the token

            p.handle(f"Attempting to confirm account [{email}]")

            start_confirmmail = time.time()

            SDEV().changeurl(rm)

            start_solvingcaptcha = time.time()
            p.solver("Solving Captcha")

            try:
                self.hit_challenge(driver, challenger=challenger, retries=10)
            except:
                pass

            self.solved += 1
            end_solvingcaptcha = time.time()
            p.solver(f"Captcha Solved in [ {end_solvingcaptcha - start_solvingcaptcha} ] seconds.")   

            end_confirmmail = time.time()
            p.handle(f"Account confirmed in [{end_confirmmail - start_confirmmail}]")

            p.session(f"Solved Captchas in this session: [ {self.solved} ]")

            discordaccount = {
                "Token": f"{token}",
                "Email Address:": f"{email}",
                "Username:": f"{username}",
                "Password:": f"{password}"
            }

            if str(token) != None:
                self.generated_accounts += 1

                with open(__info__["tokensfile"], "a", encoding="utf-8") as savedata:
                    savedata.write(f"{token}" + "\n")
                    savedata.close()

                with open(__info__["jaccfile"], "a", encoding="utf-8") as savedata:
                    json.dump(discordaccount, savedata, indent=4)
                    savedata.write("\n")
                    savedata.close()

                p.token(f"Token: [ {str(token)} ]")
                p.token(f"Email: [ {email} ]")
                p.token(f"Username: [ {str(username)} ]")
                p.token(f"Password: [ {str(password)} ]")
            else:
                p.error("Unable to create account")



            p.session(f"Generated Accounts in this session: [ {self.generated_accounts} ]")

            driver.quit()





#----------------------------------END SELENIUM GENERATOR----------------------------------









if __name__ == "__main__":
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'{__info__["appname"]} | Version: [ {__info__["version"]} ] | Proxies Loaded: [ {pcount()} ] | Last Update: [ {__info__["lastupdate"]} ]')
        tools().logo()
        tools().machine()
        tools().showmenu()
        action = input("┗──")
        if action == "1":
            threads = input("┗──<Enter number of threads>: " + reset_ansi)
            try:
                iheadless = input("┗──<Use Headless [RECOMMENDED [ Yes ] ]>: " + reset_ansi)
                    
                if iheadless.capitalize() == "No":
                    for _ in range(int(threads)):
                        gen(mailslurp_api_key).main(threads=int(threads), email=f"{ver.CreateEmail()[0]}" + '@mailslurp.com', password=tools().get_password(), username=tools().get_username(), proxy=(random.choice(list(proxylist)) if use_proxy_boolean==True else None), headless=False) #"91.246.195.196:6965"
                    time.sleep(10)
                    
                            
                elif iheadless.capitalize() == "Yes":
                    for _ in range(int(threads)):
                        gen(mailslurp_api_key).main(threads=int(threads), email=f"{ver.CreateEmail()[0]}" + '@mailslurp.com', password=tools().get_password(), username=tools().get_username(), proxy=(random.choice(list(proxylist)) if use_proxy_boolean==True else None), headless=True) #"91.246.195.196:6965"
                    time.sleep(10)
                    
                            
                else:
                    pass
                    
            except Exception as e:
                print(f"[ ERROR ] {e}")
                        
                time.sleep(100)

                
        else:
            pass
            
                


    except KeyboardInterrupt:
        p.handle("Exiting")
