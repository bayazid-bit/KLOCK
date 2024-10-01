import fitz
from threading import Thread
import itertools
import sys
import os

status = False
print_current = False
def show_banner():
    text = """\033[1;32m
                           __ __ __    ____  ________ __
                          / //_// /   / __ \/ ____/ //_/
                         / ,<  / /   / / / / /   / ,<   
                        / /| |/ /___/ /_/ / /___/ /| |  
                       /_/ |_/_____/\____/\____/_/ |_|                                     
                                    \033[31m by MD.Bayazid
                                Email: bayazid.mtu@gmail.com
            
                   \033[0m"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text)


def get_input(prompt):
    try:
        user_input = input(f"\033[34m[*] {prompt}\033[0m")
        return user_input
    except Exception as e:
        error_status(e)
        sys.exit()

def start_status(message):
    print(f"\033[34m[*] {message}\033[0m")

def success_status(message):
    print(f"\033[32m[+] {message}\033[0m")

def error_status(message):
    print(f"\033[31m[-] {message}\033[0m")

def warning_status(message):
    print(f"\033[33m[!] {message}\033[0m")

def info_status(message):
    print(f"\033[36m[#] {message}\033[0m")
def runing_status(text):
    print(f"\033[36m[~] {text}\033[0m")
    




def unlock(reader , password):
    global  sum_of_threads , status

    if reader.authenticate(password=password):
        print()
        print()
        success_status(f"Password found: {password}")
        status = True
        print()
    else:

        return

def fire(reader , password):
    try:
        t = Thread(target=lambda : unlock(reader,password))
        t.daemon = True
        t.start()
    except :
        fire(reader, password)



def crack_by_combination( min , max , chars , file):
    global sum_of_threads , print_current
    try:
        h = get_input("Show current key (it will make slower the process)<yes>/<no> ")
        if 'yes' in h:
            print_current = True
        else:
            print_current = False
        runing_status("Running brute force attack......")
        for i in range(min , max):
            for passwd in itertools.product(chars , repeat=i):
                passwd = "".join(passwd)
                if not status :

                    fire(reader=file , password=passwd)
                    if print_current:
                        print(f'\r\033[36m[~] Current key: {passwd} \033[0m',end='')



        if not status:
            print()
            warning_status('Password not in this combination , please try another combination or word list !')
    except Exception as e:
        warning_status(e)
        sys.exit()

def crack_by_word_list(file):
    global print_current
    try:
        word_file = get_input("Enter word list path : ")
        h = get_input("Show current key (it will make slower the process)<yes>/<no> ")
        if 'yes' in h:
            print_current = True
        else:
            print_current = False
        with open(word_file) as list:
            runing_status("Running brute force attack......")
            for i in list:
                i = i.replace('\n','')
                if not status :
                    fire(reader=file, password=i)
                    if print_current:
                        print(f'\r\033[36m[~] Current key: {i} \033[0m',end='')
        if not status :
            print()
            warning_status('Password not in this word list , please try another word list or combination!')
    except Exception as e:
        warning_status(e)
        sys.exit()


def main():
    try:
        show_banner()
        path = get_input("Enter pdf  file path: ")

        file = fitz.open(path)
        t = """
        [1] Crack by word list
        [2] Crack by key combination
        """
        print(t)
        method  = get_input('> ')
        if '1' in method:
            crack_by_word_list(file)
        elif '2' in method:
            chars = get_input("Enter key combination (e.g., abc123 for lowercase letters and digits): ")
            min = int(get_input('Enter min lenth of pasword: '))
            max = int(get_input("Enter max lenth of password: "))

            crack_by_combination(min , max , chars , file)
        else:
            warning_status('Invalid choice!')
            return
    except Exception as e:
        error_status(e)

while True:
    try:
        main()
        print()
        status = False
        print_current = False
    except Exception as e:
        error_status(e)
        print_current = False
        status = False
        print()
    except KeyboardInterrupt :
        print()
        warning_status('Exiting...')
        sys.exit()