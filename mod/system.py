# -*- coding: utf-8 -*-


from platform import python_compiler, python_version, python_build
from pathlib import Path as PPath
import os


class Wrapper:
    def __init__(self) -> None:
        pass
    
    @property
    def disk(self):
        pathhome = PPath.home()
        drive_letter = pathhome.drive
        return drive_letter

    
    @property
    def PYTHON(self):
        comp = python_compiler()
        pyv = python_version()
        pbu = python_build()[0]
        return[comp, pyv, pbu]
        
    


    @property
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
        
    

