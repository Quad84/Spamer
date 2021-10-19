import sys
from colorama import Fore as F
import keyboard
from time import sleep as S
import os

def Banner():
    def logo():
        os.system("cls")
        Baner =f"""{F.LIGHTCYAN_EX}
            _____________________________________________
            |  _____   _____      ____       __    __    |
            | / ____\ (  __ \    (    )      \ \  / /    |
            |( (___    ) )_) )   / /\ \      () \/ ()    |
            | \___ \  (  ___/   ( (__) )     / _  _ \    |
            |     ) )  ) )       )    (     / / \/ \ \   |
            | ___/ /  ( (       /  /\  \   /_/      \_\  |
            |/____/   /__\     /__(  )__\ (/          \) |
            |                                            |
            |       ______      ____     ________        |
            |      (_   _ \    / __ \   (___  ___)       |
            |        ) (_) )  / /  \ \      ) )          |
            |        \   _/  ( ()  () )    ( (           |
            |        /  _ \  ( ()  () )     ) )          |
            |       _) (_) )  \ \__/ /     ( (           |
            |      (______/    \____/      /__\          |
            |____________________________________________|
            {F.RED} |{F.GREEN}Github.com/Quad84{F.RED}|{F.GREEN}Alisa-Alikhani{F.RED}|{F.GREEN}@AL13A_7{F.RED}|
        """
        S(0.1)
        print(Baner)

    def menu():
        S(1)
        print(f"{F.RED}[!] {F.YELLOW}Select one of the following modes :\n")
        S(0.1)
        print(f"{F.RED}[1] {F.BLUE}Love Spam\n")
        S(0.1)
        print(f"{F.RED}[2] {F.BLUE}Hello Spam\n")
        S(0.1)
        print(f"{F.RED}[3] {F.BLUE}Bye Spam\n")
        S(0.1)
        print(f"{F.RED}[4] {F.BLUE}Trashy talk Spam\n")
        S(0.1)
        print(f"{F.RED}[5] {F.BLUE}Write yourself\n")
        S(0.1)
        print(f"{F.RED}[6] {F.BLUE}Exit\n")
        S(0.1)
    
    logo()
    menu()
    mode = input(f"{F.RED}[?]{F.LIGHTGREEN_EX} Enter Your Mode >>> ")
    if mode == "1" or mode == "01":
        love()
    elif mode == "2" or mode == "02":
        hello()
    elif mode == "3" or mode == "03":
        bye()
    elif mode == "4" or mode == "04":
        tt()
    elif mode == "5" or mode == "05":
        wy()                
    elif mode == "6" or mode == "06":
        print(f"{F.YELLOW}\nGod Luck My Friend ... :)\n")
        sys.exit() 
    else:
        Banner()


def love():
    print("Starting in 5 Sec ...")
    S(5)
    print("Starting...")
    a = 0
    while a < 10 :
        keyboard.write('I Love You Baby')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('“You make me think every time')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('I give you my world')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('Your eyes are my world')
        keyboard.press('enter')
        a = a + 1

    print("Finish")
    S(1)
    Banner()

def hello():
    print("Starting in 5 Sec ...")
    S(5)
    print("Starting...")
    a = 0
    while a < 50 :
        keyboard.write('Hello')
        keyboard.press('enter')
        S(0.5)
        a = a + 1

    print("Finish")
    S(1)
    Banner()

def bye():
    print("Starting in 5 Sec ...")
    S(5)
    print("Starting...")
    a = 0
    while a < 50 :
        keyboard.write('Bye')
        keyboard.press('enter')
        S(0.5)
        a = a + 1

    print("Finish")
    S(1)
    Banner()


def tt():
    print("Starting in 5 Sec ...")
    S(5)
    print("Starting...")
    a = 0
    while a < 10 :
        keyboard.write('heheheheh')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('xD')
        keyboard.press('enter')
        S(0.5)
        keyboard.write(':)')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('8)')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('I am Me xDD')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('<3')
        keyboard.press('enter')
        S(0.5)
        keyboard.write('Ops xD')
        keyboard.press('enter')
        a = a + 1

    print("Finish")
    S(1)
    Banner()


def wy():
    mymessage = input("\nEnter your text: ")
    print("Starting in 5 Sec ...")
    S(5)
    print("Starting...")
    a = 0
    while a < 50 :
        keyboard.write(mymessage)
        keyboard.press('enter')
        S(0.5)
        a = a + 1

    print("Finish")
    S(1)
    Banner()


Banner()

