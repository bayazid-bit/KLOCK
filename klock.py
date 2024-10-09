import fitz
from threading import Thread
import itertools
import sys
import os
import time



def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        log.info(f"Elapsed time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


status = False
print_current = False
word_mode  = False
get_argv = False

def reset():
    global  status , print_current , word_mode , get_argv
    status = False
    print_current = False
    word_mode = False
    get_argv = False


def show_help():

    text = """
    Description:
        One of the most powerful pdf file cracker that can crack pdf password .
        This tool support both  wordlist and key combination attack
        
        Warning: 
            This tool designed to recover pdf passwords. 
            Do not use it unethically . 
        
    parameters :
    
        -h --help               show this help 
        
        -w                      wordlist mode
        -f                      wordlist file path
        
        -p                      pdf file path 
        -v                      show current key (this will make the process slower)
        
        -c                      charset  mode
        -s                      charset 
        -n                      min password length
        -m                      max password length 
    
    
        examples:
            python3 klock.py -w -f ./demofiles/wordlist.txt -p ./demofiles/secure.pdf -v
            
            python3 klock.py -w -f ./demofiles/wordlist.txt -p ./demofiles/secure.pdf 
            
            
            python3 klock.py -c -s abcdef123456!@#$ -p ./demofiles/secure.pdf -n 6 -m 8 
            
            python3 klock.py -c -s abcdef123456!@#$ -p ./demofiles/secure.pdf -n 6 -m 8 -v
    
    [Thanks for try the tool]
    
    """
    print(text)
    sys.exit()



def checkContents(content :list, conteiner:list):
    conteiner = conteiner
    for cont in content:
        if cont in conteiner:
            continue
        else:
            return False
    return True



def geteliments(keys:list , conteiner:list):
    d  = {}
    try:
        for key in keys:
            i = conteiner.index(key) + 1
            e = conteiner[i]
            if key in ['-f','-p',]:

                if not os.path.exists(e):
                    print(f"[-] file {e} does not exist!")
                    sys.exit()



            elif key in ['-n','-m',]:
                i = conteiner.index(key) + 1
                e = conteiner[i]
                try:
                    e  = int(e)
                except:
                    print(f'{key} must be integer!')
                    show_help()
            else:
                e = e
            d[key] = e
    except:
        sys.exit()
    else:
        if len(d.keys())== len(keys):
            return d
        else:
            print('[*] incorrect order of argv !!!')
            show_help()



def cmdarg():
    global d
    global  get_argv
    global print_current
    global word_mode
    argv = sys.argv
    a = ['-w', '-p', '-f']
    b = ['-c', '-s','-n','-m' ,'-p']
    if '-v' in argv:
        print_current = True
    if '-h' in argv or '--help' in argv:
        show_help()


    elif checkContents(a,argv) :
        word_mode = True
        d = geteliments(a,argv)
        get_argv = True

    elif checkContents(b,argv) :
        d = geteliments(b, argv)
        get_argv = True

    else:
        show_help()

cmdarg()



def show_banner():
    text = """\033[1;32m
                           __ __ __    ____  ________ __
                          / //_// /   / __ \/ ____/ //_/
                         / .<  / /   / / / / /   / .<   
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
        log.error(e)
        sys.exit()

class Log:


    def start(self , message):
        print(f"\033[34m[*] {message}\033[0m")


    def success(self , message):
        print(f"\033[32m[+] {message}\033[0m")


    def error(self , message):
        print(f"\033[31m[-] {message}\033[0m")


    def warning(self , message):
        print(f"\033[33m[!] {message}\033[0m")


    def info(self , message):
        print(f"\033[36m[*] {message}\033[0m")


    def runing(self , text):
        print(f"\033[36m[~] {text}\033[0m")


def unlock(reader, password):
    global sum_of_threads, status

    if reader.authenticate(password=password):
        print()
        print()
        log.success(f"Password found: {password}")
        status = True
        print()
    else:

        return


def fire(reader, password):
    try:
        t = Thread(target=lambda: unlock(reader, password))
        t.daemon = True
        t.start()
    except KeyboardInterrupt :
        log.warning('Exiting...')
        sys.exit()
    except :
        fire(reader, password)

@timer
def crack_by_combination(min, max, chars, file):
    global sum_of_threads, print_current
    try:

        log.runing("Running brute force attack......")
        for i in range(min, max):
            for passwd in itertools.product(chars, repeat=i):
                passwd = "".join(passwd)
                if not status:

                    fire(reader=file, password=passwd)
                    if print_current:
                        print(f'\r\033[36m[~] Current key: {passwd} \033[0m', end='')

        if not status:
            print()
            log.warning('Password not in this combination , please try another combination or word list !')
    except Exception as e:
        log.warning(e)
        sys.exit()

@timer
def crack_by_word_list(file,word_file):

    try:

        with open(word_file) as list:
            log.runing("Running brute force attack......")
            for i in list:
                i = i.replace('\n', '')
                if not status:
                    fire(reader=file, password=i)
                    if print_current:
                        print(f'\r\033[36m[~] Current key: {i} \033[0m', end='')
        if not status:
            print()
            log.warning('Password not in this word list , please try another word list or combination!')
    except Exception as e:
        log.warning(e)
        sys.exit()


def main():
    global print_current
    try:
        if not get_argv:
            show_banner()
            path = get_input("Enter pdf  file path: ")

            file = fitz.open(path)
            t = """
            [1] Crack by word list
            [2] Crack by key combination
            """
            print(t)
            method = get_input('> ')
            h = get_input("Show current key (it will make slower the process)<yes>/<no> ")
            if 'yes' in h:
                print_current = True
            else:
                print_current = False
            if '1' in method:

                crack_by_word_list(file)

            elif '2' in method:
                chars = get_input("Enter key combination (e.g., abc123 for lowercase letters and digits): ")
                min = int(get_input('Enter min lenth of pasword: '))
                max = int(get_input("Enter max lenth of password: "))

                crack_by_combination(min, max, chars, file)

            else:
                log.warning('Invalid choice!')
                return
        else:
            show_banner()
            if word_mode:
                word_file = d['-f']
                pdf_file = d['-p']
                file = fitz.open(pdf_file)
                try:
                    crack_by_word_list(file, word_file)
                except Exception as e:
                    log.error(e)
            else:
                min = d['-n']
                max = d['-m']
                chars = d['-s']

                pdf_file  = d['-p']

                file = fitz.open(pdf_file)
                try:
                    crack_by_combination(min , max,chars,file)
                except Exception  as e:

                    log.error(e)

    except Exception as e:

        log.error(e)


log = Log()

while True:
    try:
        main()
        print()
        b = get_input('Type exit to close or press enter to run again: ')
        if 'exit' in b:
            sys.exit()
        print()
        reset()
    except Exception as e:
        log.error(e)
        print()
        b = get_input('Type exit to close or press enter to run again: ')
        if 'exit' in b:
            sys.exit()
        reset()

    except KeyboardInterrupt:
        print()
        log.warning('Exiting...')
        sys.exit()
