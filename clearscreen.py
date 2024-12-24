import os
import platform

def clear_screen():                     #clears te screen with a different command depending on your operating system
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")