from SimpleQIWI import *
from colorama import Fore
print(Fore.RED + '   ОШИБКИ')
print('1.Недостаточно средств')
print('2.Неправильный токен/Номер')
print('3.Пользователь Заблокирован')
print('4.У токена нет всех рарешений')
print()
token=input("Введите токен: ")
youphone=input("Номер на который отправяться деньги: ")
phone=input("Введите номер QIWI: ");
kommentari=input("Введите коментарий: ")
money=input("Введите сумму: ")
api = QApi(token=token, phone=phone)

print(api.balance)

api.pay(account=youphone, amount=money, comment=kommentari)

print(api.balance)
while True:
    exit = int(input('<$>'))
    try:
        if exit == 0:
            print(Fore.GREEN + 'Переход на глав.меню ->')
            sleep(2)
            import QuickQiwi.py
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import QuickQiwi.py
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        import QuickQiwi.py
input()
