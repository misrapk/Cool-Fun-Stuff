from time import sleep
from random import randint
from colorama import Fore, Style
text1 = input("Enter holiday message: ")
text1 = str(text1)
base1 = len(text1)
base1 += 1
while True:
    print('\033c')
    for x in range(1, base1, 2):
        y = randint(2,12)
        if x ==1:
            print(Style.BRIGHT+Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y%5 == 0:
            print(Fore.RED + "{:^40}".format(text1[:x]))
        elif y%3 ==0:
            print(Fore.GREEN + "{:^40}".format(text1[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text1[:x]))
            
    print(Fore.WHITE+"{:^39}".format("||||"))
    print(Fore.WHITE+"{:^39}".format("||||"))
    sleep(.50)    