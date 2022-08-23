import os
import sys
import colorama
import time
from time import sleep
from colorama import init, Fore, Back
init(autoreset=True)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Back.GREEN + '+', Back.BLACK + "                                              ", Back.GREEN + '+')
print(Back.GREEN + ' ', Back.BLACK + "   ____            _          _       ____    _              _  ", Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + "  / __ \          (_)        | |     / __ \  (_)            (_) " , Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + " | |  | |  _   _   _    ___  | | __ | |  | |  _  __      __  _ " + ' ', Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + " | |  | | | | | | | |  / __| | |/ / | |  | | | | \ \ /\ / / | |",  Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + " | |__| | | |_| | | | | (__  |   <  | |__| | | |  \ V  V /  | |",  Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + "  \___\_\  \__,_| |_|  \___| |_|\_\  \___\_\ |_|   \_/\_/   |_|", Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.GREEN + "      ░   ░     ░ ░     v0.5 ░ ░ ░          ", Back.GREEN + ' ')
print(Back.GREEN + ' ', " ====░=====░=====░==░=░======░=░=====░=====░==", Back.GREEN + ' ')
print(Back.GREEN + ' ', "        Made by:", Fore.CYAN + "BeanD                 " + '      ', Back.GREEN + ' ')
print(Back.GREEN + ' ', "        Updates:", Fore.CYAN + "https://t.me/pipiska228" + '      ', Back.GREEN + ' ')
print(Back.GREEN + ' ', " =============================================", Back.GREEN + ' ')
print(Back.GREEN + ' ', Back.BLACK + "                                              ", Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.YELLOW  + "                  Инструменты" + '                 ', Back.GREEN + ' ')
print(Back.GREEN + ' ', Back.BLACK + "                                              ", Back.GREEN + ' ')
print(Back.GREEN + ' ', Back.BLACK + '      ' + Back.RED + '!' + Back.BLACK + '                ' + Back.BLACK + '                        ' + Back.GREEN + " ")
print(Back.GREEN + ' ', Fore.LIGHTMAGENTA_EX  + " 1.[1000-7]       2.[Qiwi]       3.[GENUS-IP]" + ' ', Back.GREEN + ' ')
print(Back.GREEN + ' ', Back.BLACK + "                                              ", Back.GREEN + ' ')
print(Back.GREEN + ' ', Fore.MAGENTA  + " '''''''''''''''''''''''''''''''''''''''''''' ", Back.GREEN + ' ')
while True:
    inp = int(input(Back.BLACK + ' ' + Back.BLACK + '  <$> ' + Fore.LIGHTBLACK_EX))
    try:
        if inp == 1:
            print(Fore.GREEN + 'Вы выбрали [1000-7]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import index.py
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 2:
            print(Fore.GREEN + 'Вы выбрали [Qiwi]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import QiwiII.py
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 3:
            print(Fore.GREEN + 'Вы выбрали [GENUS-IP]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import GS.py
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)




input()