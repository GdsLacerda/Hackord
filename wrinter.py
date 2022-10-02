# -*- coding: utf-8 -*-

import os, sys
try:
    import datetime, time
    from pystyle import Colorate , Colors
    from colorama import Style, Fore
except ImportError:
    os.system("pip install -r requirements.txt")

__info__ = {
    "logspath": "logs/logs.log"
    }

class wrint():

    def __init__(self):
        #super(Wrint, self).__init__()
        self.Time = Style.BRIGHT
        self.Warning = Fore.YELLOW
        self.Error = Fore.LIGHTRED_EX
        self.Critical = Fore.RED
        self.Debug = Fore.LIGHTMAGENTA_EX
        self.Info = Fore.LIGHTBLUE_EX
        self.Ok = Fore.GREEN
        self.Success = Fore.LIGHTGREEN_EX
        self.RESET = Style.RESET_ALL
    

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
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ SESSION ] >" + " " + f"{text}", 1) + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.green_to_yellow, f"[ SESSION ] >" + " " + f"{text}", 1) + self.RESET


    def token(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ TOKEN ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            pass
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ TOKEN ] >" + " " + f"{text}", 1) + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.red_to_purple, f"[ TOKEN ] >" + " " + f"{text}", 1) + self.RESET



    def solver(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SOLVER ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.green_to_red, f"[ SOLVER ] >" + " " + f"{text}", 1) + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.green_to_red, f"[ SOLVER ] >" + " " + f"{text}", 1) + self.RESET


    def handle(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ HANDLE ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.blue_to_cyan, f"[ HANDLE ] >" + " " + f"{text}", 1) + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + self.RESET + " " + Colorate.Horizontal(Colors.blue_to_cyan, f"[ HANDLE ] >" + " " + f"{text}", 1) + self.RESET 


    def info(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ INFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Info + "[ INFO ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Info + "[ INFO ] >" + " " + f"{text}" + self.RESET


    def warning(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ WARNING ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Warning + "[ WARNING ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Warning + "[ WARNING ] >" + " " + f"{text}" + self.RESET


    def debug(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ DEBUG ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Debug + "[ DEBUG ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Debug + "[ DEBUG ] >" + " " + f"{text}" + self.RESET


    def critical(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Critical + "[ CRITICAL ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Critical + "[ CRITICAL ] >" + " " + f"{text}" + self.RESET


    def error(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Error + "[ ERROR ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Error + "[ ERROR ] >" + " " + f"{text}" + self.RESET


    def ok(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ OK ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Ok + "[ OK ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Ok + "[ OK ] >" + " " + f"{text}" + self.RESET

    
    def success(self, text: str = None, return_only: bool = False) -> str:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SUCCESS ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        if return_only != True:
            print(self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Success + "[ SUCCESS ] >" + " " + f"{text}" + self.RESET)
        return self.RESET + self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Success + "[ SUCCESS ] >" + " " + f"{text}" + self.RESET
