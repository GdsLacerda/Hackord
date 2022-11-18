# -*- coding: utf-8 -*-
# >>> ANSI CODES <<<
# >>> Colored Output <<<

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