import siteName  # инициализация нашего модуля
import time
import sys
import os
import datetime
# Function for implementing the loading animation
def load_animation():
    # String to be displayed when the application is loading
    load_str = "GENUS IP"
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0

    while (counttime != 100):

        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    # for windows OS
    if os.name == "nt":
        os.system("cls")

    # for linux / Mac OS
    else:
        os.system("clear")


# Driver program
if __name__ == '__main__':
    load_animation()

    # Your desired code continues from here
    # s = input("Enter your name: ")
    s = (datetime.date.today())
    sys.stdout.write("Дата запуска: " + str(s) + "\n")

print("                             ,--.")
print("  ,----..       ,---,.       ,--.'|               .--.--.")
print(" /   /   \    ,'  .' |   ,--,:  : |         ,--, /  /    '.")
print("|   :     : ,---.'   |,`--.'`|  ' :       ,'_ /||  :  /`. /")
print(".   |  ;. / |   |   .'|   :  :  | |  .--. |  | :;  |  |--`")
print(".   ; /--`  :   :  |-,:   |   \ | :,'_ /| :  . ||  :  ;_")
print(";   | ;  __ :   |  ;/||   : '  '; ||  ' | |  . . \  \    `.")
print("|   : |.' .'|   :   .''   ' ;.    ;|  | ' |  | |  `----.   \ ")
print(".   | '_.' :|   |  |-,|   | | \   |:  | | :  ' ;  __ \  \  | ")
print("'   ; : \  |'   :  ;/|'   : |  ; .'|  ; ' |  | ' /  /`--'  / ")
print("'   | '/  .'|   |    \|   | '`--'  :  | : ;  ; |'--'.     / ")
print("|   :    /  |   :   .''   : |      '  :  `--'   \ `--'---' ")
print(" \   \ .'   |   | ,'  ;   |.'      :  ,      .-./ ")
print("  `---`     `----'    '---'         `--`----' ")






getIPaddr = siteName.getIP
getServer = siteName.getServerName
modulesList = r"""

            +-----------------------------------------+
            | [1] -- Получить IP-адресс сервера.      |
            | [2] -- Получить название сервера.       |
            +-----------------------------------------+

"""
# выводим список некоторых команд
print(r"""

            +-----------------------------------------+
            | [B] -- Возвращает вас на один шаг назад |
            | [O] -- Посмотреть возможности           |
            +-----------------------------------------+

""")


# список модулей
def setModule():  # функция направлена на выбор и использование модулей

    moduleNum = input("[Введите число]: ")

    if moduleNum == "1":

        try:
            domain = input("[Введите домен]: ")  # запрашиваем у пользователя имя сайта
            ipSite = getIPaddr(domain)  # отправляем имя нашему модулю

            print("-" * 60)
            print("[IP] == [{0}]".format(ipSite))
            print("-" * 60)

        except:
            print("[Error]: Домен не найден!")


    elif moduleNum == "2":

        try:
            site = input("[Введите IP-адресс]: ")
            url = "http://" + site
            server = getServer(url)

            print("-" * 60)
            print("[Server] == [{0}]".format(server))
            print("-" * 60)

        except:
            print("[Error]: Адресс не найден!")

    comand()


def comand():  # функция направлена на исполнение выбранной пользователем команды

    comand = input("[$] --> ")

    if comand == "B":
        print("Вы успешно вышли")
        import Silion.py
    elif comand == "O":

        print(modulesList)
        print(setModule())

    else:

        print("[Error]: Команда не найдена!")
        exit("Код остановлен!")


print(comand())
