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
from os import system
from core.colors import Color

# Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
if os.name == "nt" and platform.release() == "10" and platform.version() >= "10.0.14393":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def clear():
    if os.name == "nt":
        system("cls")
    else:
        system("clear")


def noConnection():
    print("""{}
   ,_       
 ,'  `\,_   
 |_,-'_)    
 /##c '\  ( 
' |'  -{.  )
  /\__-' \[]
 /`-_`\     
 '     \ 
                [!] No network connection found. 
    {}""".format(Color.RED, Color.END))
    exit(0)

def badPython():
    print("{}Please use Python 3. $ python3 TOTB.py{}".format(Color.RED, Color.END))


def welcome():
    print("""{}
                         d8b      
   d8P             d8P   ?88      
d888888P        d888888P  88b     
  ?88'   d8888b   ?88'    888888b 
  88P   d8P' ?88  88P     88P `?8b
  88b   88b  d88  88b    d88,  d88
  `?8b  `?8888P'  `?8b  d88'`?88P'
    
    Multi-board image downloader!                           
    {}""".format(Color.RED, Color.END))


def end():
    print("{}Goodbye.{}".format(Color.BLUE, Color.END))

