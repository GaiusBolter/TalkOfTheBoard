######################################################
#                                                    #
#       TalkOfTheBoard - 0.0.1                       #
#                                                    #
#       by:     Splendid                             #
#                                                    #
#                                                    #
######################################################

import platform
import os
from core.colors import Color

# Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
if os.name == "nt" and platform.release() == "10" and platform.version() >= "10.0.14393":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

menu_options = [
        "Scrape",
        "Options"
]

TOTB_PROMPT = "{}TOTB => {}".format(Color.GREEN, Color.END)


def user_input(prompt, options: list):
    while True:
        response = input(prompt)
        if response.isdigit():
            print(options[int(response)])
        if type(response) == str:
            if response in options:
                print(response)


def get_options(prompt: str, options: list):
    opid = 0
    for option in options:
        print(opid, Color.PINK, option, Color.END)
        opid += 1
    else:
        user_input(TOTB_PROMPT, options)

