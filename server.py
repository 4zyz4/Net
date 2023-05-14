import datetime
import time
import os
os.system('sudo /etc/init.d/shadowsocks start')
while 1:
    os.system('clear')
    now=datetime.datetime.now()
    print(now.strftime("[%Y-%m-%d %H:%M:%S]"))
    os.system('free')
    os.system('sudo /etc/init.d/shadowsocks status')
    time.sleep(1)
