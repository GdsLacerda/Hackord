# -*- coding: utf-8 -*-

from pystyle import Colors, Colorate
import time, sys, json
from datetime import datetime

reset_ansi = '\033[0m'


cfgfile = open("./data/config.json").read()
config = json.loads(cfgfile) 





class printf():

    def __init__(self):
        super(printf, self).__init__()
        try:
            self.printlog = config["Logs"]["hackord-log"]
        except:
            self.printlog = "logs/hackord.log"
        
    

    def aprint(self, text: str = None, t: float = 0.01) -> None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(t)
        print("\n")
        

    def proxyscraper(self, text: str = None):
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ PROXYSCRAPER ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_cyan, f"[ PROXYSCRAPER ] >" + " " + f"{text}",1) + reset_ansi)
        
    def ratelimit(self, text: str = None):
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN/RATE_LIMITED ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_red, f"[ RATE_LIMIT ] >" + " " + f"{text}",1) + reset_ansi)
    
    
    
    class DiscordToken:
        def __init__(self) -> None:
            self.printlog = config["Logs"]["hackord-log"]
            
        def valid(self, text: str = None):
            try:
                with open(file=f"{self.printlog}", mode="a+") as logfile:
                    logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN/VALID ] >" + " " + f"{text}" + "\n")
                    logfile.close()
            except Exception as e:
                print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ TOKEN/VALID ] >" + " " + f"{text}",1) + reset_ansi)
            
            
        def locked(self, text: str = None):
            try:
                with open(file=f"{self.printlog}", mode="a+") as logfile:
                    logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN/LOCKED ] >" + " " + f"{text}" + "\n")
                    logfile.close()
            except Exception as e:
                print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_yellow, f"[ TOKEN/LOCKED ] >" + " " + f"{text}",1) + reset_ansi)
            
            
        def invalid(self, text: str = None):
            try:
                with open(file=f"{self.printlog}", mode="a+") as logfile:
                    logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN/INVALID ] >" + " " + f"{text}" + "\n")
                    logfile.close()
            except Exception as e:
                print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ TOKEN/INVALID ] >" + " " + f"{text}",1) + reset_ansi)
            
            
        def ratelimited(self, text: str = None):
            try:
                with open(file=f"{self.printlog}", mode="a+") as logfile:
                    logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN/RATE_LIMITED ] >" + " " + f"{text}" + "\n")
                    logfile.close()
            except Exception as e:
                print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
            print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_red, f"[ TOKEN/RATE_LIMITED ] >" + " " + f"{text}",1) + reset_ansi)



    def solver(self, text: str = None, end: any = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SOLVER ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.blue_to_purple, f"[ SOLVER ] >" + " " + f"{text}",1) + reset_ansi, end=end)


    def handle(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ HANDLE ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_green, f"[ HANDLE ] >" + " " + f"{text}",1) + reset_ansi)


    def info(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ INFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.cyan_to_blue, f"[ INFO ] >" + " " + f"{text}",1) + reset_ansi)


    def warning(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ WARNING ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ WARNING ] >" + " " + f"{text}",1) + reset_ansi)


    def debug(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ DEBUG ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.white_to_blue, f"[ DEBUG ] >" + " " + f"{text}",1) + reset_ansi)



    def error(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ ERROR ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.red_to_white, f"[ ERROR ] >" + " " + f"{text}",1) + reset_ansi)


    def ok(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ OK ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_blue, f"[ OK ] >" + " " + f"{text}",1) + reset_ansi)

    
    def success(self, text: str = None) -> str:
        try:
            with open(file=f"{self.printlog}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SUCCESS ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(reset_ansi + Colorate.Horizontal(Colors.white_to_black, f"[ {datetime.now().strftime('%H:%M:%S')} ]",1) + reset_ansi + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ SUCCESS ] >" + " " + f"{text}",1) + reset_ansi)


