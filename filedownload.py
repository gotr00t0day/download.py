import requests, sys, socket, os, hashlib, shutil, random, time
from random import randint
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
from os import path

# filedownload v1.0 by c0deninja

if len(sys.argv) !=3:
    print("Usage: download site filename")
    sys.exit(1)

def sockproxies():
    socks5 = "184.178.172.13:15311"
    socks52 = "184.178.172.25:15291"
    
    proxies = {
        "socks5" : socks5,
        "socks52" : socks52
        }

def downloadfile():
    site = sys.argv[1]
    filename = sys.argv[2]

    if "http" in site:
        site = site.replace("http://", "")
    elif "https" in site:
        site = site.replace("https://", "")
    
    try:
        ua = UserAgent()
        header = {'User-Agent':str(ua.chrome)} 
        r = requests.get(sys.argv[1], headers=header, proxies=sockproxies()) 
        if r.status_code == 200:
            print ("HTTP request sent, awaiting response.. 200 OK")
            print (f'Saving to: {filename}')
            if os.path.isfile(filename):
                fileexist = input(f'{filename} exists, do you want to overwrite it?? [y/n]: ').lower()
                if fileexist == 'y':
                    with open(filename, 'wb') as download:
                        download.write(r.content)
                if fileexist == 'n':
                    num = 0
                    num += 1
                    newfile = "{}({})".format(filename,num)
                    print("Making a copy of {}....".format(filename))    
                    time.sleep(1)
                    os.popen('copy {} {}'.format(filename, newfile))
                    print(f'{newfile}({num}) copied!')
            if not os.path.isfile(filename):
                with open(filename, 'wb') as f:
                    f.write(r.content)
            if os.path.isfile(filename):
                statinfo = os.stat(filename)
                size = statinfo.st_size
                print (f'Size: {size}')
                checksum = hashlib.md5(open(filename, 'rb').read()).hexdigest()
                print (f'MD5: {checksum}')
                print (f'{filename} successfully saved')
            if not os.path.isfile(filename):
                print (f'{filename} could not be saved')
        elif r.status_code == 400:
            print (Fore.RED + "Bad Request")
        elif r.status_code == 404:
            print (Fore.RED + "Not Found")
        elif r.status_code == 403:
            print (Fore.RED + "Forbidden")
    except requests.exceptions.ConnectionError:
        print (Fore.RED + "name or service not known")

if __name__ == "__main__":
    downloadfile()
