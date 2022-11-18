# -*- coding: utf-8 -*-
# > Hackord V2 | 1.0 <
# > License : GPL V2
# > Source Code
# > By LefeuWare > Lefeu > https://"website_coming soon"
# > WARNING: DO NOT REUSE THIS SOURCE CODE FOR NON-EDUCATIONAL PURPOSES
# > DISCLAIMER: EDUCATIONAL PURPOSES ONLY
# > Discord: ( https://discord.gg/KCqrbVgSBF )

VERSION = "2.0.4-AAV"

import threading, sys, time, json, random, os, platform

from pystyle import Colorate, Colors

from mod.setup import Setup

if os.path.exists(os.path.join(f"{os.getcwd()}", "logs")) != True:
    Setup().run
    print("PLEASE RELAUNCH HACKORD V2")
    print("Closing this window in 3 seconds...")
    time.sleep(3.3)
    sys.exit()




from mod.discordapi import DiscordAPI
from mod.system import Wrapper
from mod.printf import printf
from mod.proxyscraper import Scraper
from mod.nitrominer import Nitro, _get_nitro_code

p = printf()
    
cfgfile = open("data/config.json").read()
config = json.loads(cfgfile)


if os.path.exists(os.path.join(f"{os.getcwd()}", "logs")) == True:
    if os.path.exists(f"{config['Chromedriver']['chromedriver-path']}") != True:
        Setup().download_chromedriver





     
      
# > Proxy Service Class > Fortmatting > Read porxyfile > Requires config.json Access! > load > count < 
class ProxyService:
    def __init__(self) -> None:
        super(ProxyService, self).__init__()
        self.proxyfile = config['Proxies']['proxy_file'] # > Proxy File [ config.json ]
        self.proxyformat = lambda proxytype, proxy: {f"all://": f"{proxytype}://{proxy}"} # > HTTPX Proxy Formatting [ https://www.python-httpx.org/compatibility/ ]
        self.proxy_list = []
    
    @property
    def load(self):
        with open(self.proxyfile) as readproxy:
            lines = readproxy.readlines()
            for proxy in lines:
                self.proxy_list.append(proxy.replace("\n", ""))
    
    @property
    def count(self):
        return len(self.proxy_list)
        
     




class TokensService:
    def __init__(self) -> None:
        super(TokensService, self).__init__()
        self.tokens_in = config["Tokens"]["tokens-file"]
        self.tklist = []

    @property
    def load(self):
        with open(self.tokens_in) as readtk:
            lines = readtk.readlines()
            for token in lines:
                self.tklist.append(token.replace("\n", ""))

    @property
    def count(self):
        return len(self.tklist)
        

     


ps = ProxyService()
ps.load 
proxycount = ps.count

ts = TokensService()
ts.load
tokens_loaded = ts.count





            
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
            
            
            
            
            
            

            
class Menu:
    def __init__(self):
        self.introduce = fr"""
                                        ╔══════════════════════════════════╗
                                        ║      {ANSI().Purple}Hackord V2 [ {VERSION} ]{ANSI().Reset}    ║ 
                                        ║             {ANSI().Purple}By Lefeu{ANSI().Reset}             ║  
                                        ║            {ANSI().Purple}OS : {platform.system()}{ANSI().Reset}          ║
                                        ║   {ANSI().Red}https://discord.gg/KCqrbVgSBF{ANSI().Reset}  ║ 
                                        ║      {ANSI().Green}BEST DISCORD HACK TOOL{ANSI().Reset}      ║ 
                                        ╚══════════════════════════════════╝
"""
        self.logo = Fr"""
                    ██╗  ██╗ █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗██████╗ 
                    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║╚════██╗
                    ███████║███████║██║     █████╔╝ ██║   ██║██████╔╝██║  ██║    ██║   ██║ █████╔╝
                    ██╔══██║██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██╔═══╝ 
                    ██║  ██║██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝ ███████╗
                    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝  ╚══════╝  
                                                                                                       
"""                                         
        self.menu = FR""" 
                            ┌────────*Discord*──────────┬────────*Extra*─────────┐
                            │ {ANSI().Red}[{ANSI().Reset}{ANSI().Blue} 1 {ANSI().Red}] {ANSI().Cyan}Token Generator{ANSI().Reset}     │ {ANSI().Red}[{ANSI().Reset}{ANSI().Blue} 10 {ANSI().Red}] {ANSI().Cyan}Proxy Scraper{ANSI().Reset}   │ 
                            │ {ANSI().Red}[{ANSI().Reset}{ANSI().Blue} 2 {ANSI().Red}] {ANSI().Cyan}Token Joiner{ANSI().Reset}        │                        │ 
                            │ {ANSI().Red}[{ANSI().Reset}{ANSI().Blue} 3 {ANSI().Red}] {ANSI().Cyan}Token Checker{ANSI().Reset}       │                        │ 
                            │ {ANSI().Red}[{ANSI().Reset}{ANSI().Blue} 4 {ANSI().Red}] {ANSI().Cyan}Nitro Miner{ANSI().Reset}         │                        │             
                            └───────────────────────────┴────────────────────────┘
                            
"""

    @property
    def clear(self):
        Wrapper().clear

    
    def run(self):
        while True:

            choice = None
        
            print(self.introduce)
            
            print(Colorate.Diagonal(Colors.white_to_blue, self.logo, 3)) # > Hackord Logo

            print(self.menu) # > Hackord Menu
            

            if ps.proxy_list == []:
                p.warning("THIS TOOL CAN'T WORK WITHOUT PROXIES! PLEASE INPUT PROXIES IN DATA/PROXIES.TXT THANKS!")

            choice = input(f"                                           {ANSI().Green}[ {ANSI().Cyan}? {ANSI().Green}] Enter Choice > {ANSI().Reset}") # > Input > Action

            if choice.isnumeric() == True:
            
                if int(choice) == 1:
                    Wrapper().clear

                    def printtokengen():
                        return (ANSI().Yellow + fr"""

   ▄▄▄▄▀ ████▄ █  █▀ ▄███▄      ▄         ▄▀  ▄███▄      ▄   
▀▀▀ █    █   █ █▄█   █▀   ▀      █      ▄▀    █▀   ▀      █  
    █    █   █ █▀▄   ██▄▄    ██   █     █ ▀▄  ██▄▄    ██   █ 
   █     ▀████ █  █  █▄   ▄▀ █ █  █     █   █ █▄   ▄▀ █ █  █ 
  ▀              █   ▀███▀   █  █ █      ███  ▀███▀   █  █ █ 
                ▀            █   ██                   █   ██ 
                                                                  
""" + ANSI().Reset)
                    print(printtokengen())
                    threads = input("[ TOKEN_GENERATOR ] --> Enter Threads [ NUMBER_REQUIRED ] :> ")
                    use_threading = input("[ TOKEN_GENERATOR ] --> Use Threading [EXPERIMENTAL] [ Y / N ] :> ").capitalize()
                    t1 = time.time()

                    if use_threading == "Y":
                        for _ in range(int(threads)):
                            Wrapper().clear
                            print(printtokengen())
                            p.info(f"Reading proxies from file: [ {config['Proxies']['proxy_file']} ]")
                            t = threading.Thread(target=DiscordAPI().Register(proxy=ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}")))
                            t.start() 
                    elif use_threading == "N":
                        for _ in range(int(threads)):
                            Wrapper().clear
                            print(printtokengen())
                            p.info(f"Reading proxies from file: [ {config['Proxies']['proxy_file']} ]")
                            DiscordAPI().Register(proxy=ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}"))

                    else:
                        Wrapper().clear

                    

                    t2 = time.time()
                    p.info(f"Generator work time: [ {t2-t1} ]")
                    p.debug("Returning to menu in 10 seconds...")
                    time.sleep(13)
                    Wrapper().clear
                    
                if int(choice) == 2:
                    Wrapper().clear
                    print(ANSI().Red + fr"""
                    
   ▄▄▄▄▀ ████▄ █  █▀ ▄███▄      ▄         ▄▄▄▄▄ ████▄ ▄█    ▄   ▄███▄   █▄▄▄▄ 
▀▀▀ █    █   █ █▄█   █▀   ▀      █      ▄▀  █   █   █ ██     █  █▀   ▀  █  ▄▀ 
    █    █   █ █▀▄   ██▄▄    ██   █         █   █   █ ██ ██   █ ██▄▄    █▀▀▌  
   █     ▀████ █  █  █▄   ▄▀ █ █  █      ▄ █    ▀████ ▐█ █ █  █ █▄   ▄▀ █  █  
  ▀              █   ▀███▀   █  █ █       ▀            ▐ █  █ █ ▀███▀     █   
                ▀            █   ██                      █   ██          ▀    
                                                                              
""" + ANSI().Reset)
                    
                    p.info(f"Reading tokens from file: [ {config['Tokens']['tokens-file']} ]")
                    p.info(f"Reading proxies from file: [ {config['Proxies']['proxy_file']} ]")
                    ic = input("[ TOKEN_JOINER ] --> Enter Discord Invite Code [ STRING ] :> ")
                    p.ok(f"Attempting to join [ {tokens_loaded} ] to [ {ic} ]")
                    start_joiner = time.time()
                    for token in ts.tklist:
                        DiscordAPI().JoinGuild(token, ic, ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}"))
                    end_joiner = time.time()
                    p.ok(f"Joiner session [ {end_joiner-start_joiner} ]")
                    p.debug("Returning to menu in 10 seconds...")
                    time.sleep(13)
                    Wrapper().clear
                    
                else:
                    Wrapper().clear



                                                                                    

            if int(choice) == 3:
                Wrapper().clear
                print(ANSI().Red + fr"""
                
   ▄▄▄▄▀ ████▄ █  █▀ ▄███▄      ▄       ▄█▄     ▄  █ ▄███▄   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄ 
▀▀▀ █    █   █ █▄█   █▀   ▀      █      █▀ ▀▄  █   █ █▀   ▀  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀ 
    █    █   █ █▀▄   ██▄▄    ██   █     █   ▀  ██▀▀█ ██▄▄    █   ▀  █▀▄   ██▄▄    █▀▀▌  
   █     ▀████ █  █  █▄   ▄▀ █ █  █     █▄  ▄▀ █   █ █▄   ▄▀ █▄  ▄▀ █  █  █▄   ▄▀ █  █  
  ▀              █   ▀███▀   █  █ █     ▀███▀     █  ▀███▀   ▀███▀    █   ▀███▀     █   
                ▀            █   ██              ▀                   ▀             ▀    
                                                                                        
""" + ANSI().Reset)
                p.info("Token checker started")
                ctime1 = time.time()
                for token in ts.tklist:
                    print(token)
                    DiscordAPI().Login(token, ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}"))
                ctime2 = time.time()
                p.ok(f"Token Checking Time [ {ctime2-ctime1} ]")
                p.debug("Returning to menu in 10 seconds...")
                time.sleep(13)
                Wrapper().clear

            
            if int(choice) == 10:
                print(fr"""
                        
            ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    
            ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    
            ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     
            ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      
            ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       
            ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       
                                                        
        ███████╗██████╗  █████╗ ██████╗ ███████╗██████╗   
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  
        ███████╗██████╔╝███████║██████╔╝█████╗  ██████╔╝  
        ╚════██║██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗  
        ███████║██║  ██║██║  ██║██║     ███████╗██║  ██║  
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝  
                                                        
                """)
                Scraper().scrape()
                p.debug("Returning to menu in 7 seconds...")
                time.sleep(7.8)
                Wrapper().clear


            if int(choice) == 4:
                print(fr"""{ANSI().Purple}
                        
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████      ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░    ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░    ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
         ░  ░              ░         ░ ░            ░    ░           ░    ░  ░   ░     
                                                                                         
                {ANSI().Reset}""")
                NITROCODE = input(f"{ANSI().Red}[{ANSI().Reset} {ANSI().Yellow}#{ANSI().Reset} {ANSI().Red}]{ANSI().Reset} {ANSI().Yellow}Enter Nitro type to generate, classic or boost?{ANSI().Reset}\n{ANSI().Blue}[ ( 1 ) for nitro classic, ( 2 ) for nitro boost ]{ANSI().Reset} :>")
                print(f"{ANSI().Purple}[{ANSI().Reset} {ANSI().Cyan}#{ANSI().Reset} {ANSI().Purple}]{ANSI().Reset} {ANSI().Cyan}Okey!{ANSI().Reset}")
                acc_to_gen = input(f"{ANSI().Blue}[{ANSI().Reset} {ANSI().Yellow}#{ANSI().Reset} {ANSI().Blue}]{ANSI().Reset} {ANSI().Yellow}Enter number of nitro codes to generate & check.{ANSI().Reset}\n{ANSI().Blue}[ Number is required]{ANSI().Reset} :>")

                for _ in range(int(acc_to_gen)):
                    if Nitro().NitroMiner(ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}"), _get_nitro_code(int(NITROCODE))) == False:
                        Nitro().NitroMiner(ps.proxyformat(f"{config['Proxies']['type']}", f"{random.choice(ps.proxy_list)}"), _get_nitro_code(int(NITROCODE)))
                        


            else:
                Wrapper().clear
                
                


                
                

                
if __name__ == "__main__":
    try:
        Wrapper().clear
        if os.path.exists(config["Chromedriver"]["chromedriver-path"]):
            title = (f"Process: [ Hackord V2 ] | PID: [ {os.getpid()} ] | Proxies: [ {proxycount} ] | Tokens: [ {tokens_loaded} ]")
            print(f'\33]0;{title}\a', end='', flush=True)
        else:
            title = (f'Process: [ Hackord V2 ] | PID: [ {os.getpid()} ] | Proxies: [ {proxycount} ] | Tokens: [ {tokens_loaded} ] | Warning!: [ {config["Chromedriver"]["chromedriver-path"]} not exists! ]')
            print(f'\33]0;{title}\a', end='', flush=True)
        Menu().run()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        #raise Exception
        p.error(f"Unhandled Error: [ {e} ]")
        p.debug("QUICK FIX: [ Relaunch Hackord and try again / Report error on our Discord Server ]")

else:
    title = f"Process: [ HackordV2 ] | Allowed: [ ABORT ]"
    print(f'\33]0;{title}\a', end='', flush=True)
    time.sleep(1000)
        

        
      
