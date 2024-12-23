import os
import platform

def clear_screen():
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")