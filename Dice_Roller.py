# Programmed by: Mubashir Ahmed OR known as Mubashir78 on GitHub
# https://www.github.com/Mubashir78

from time import sleep
from random import randint
SLEEP = 1

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

error_code = color.BOLD+color.UNDERLINE+color.RED+"Invalid input. Try again."+color.END


def sub_main():
    val_of_roll = randint(1,6)
    print(" ")
    print(f"{'o' * val_of_roll : ^31}")
    print(color.ITALIC+color.GREEN+f"         Rolled a {val_of_roll} !"+color.END)
    while True:
        print(" ")
        y = input(color.BOLD+"Do you wish to reroll? (y/n): "+color.END).lower()
        if y == "y":
            return sub_main()
        elif y == "n":
            print("======================================================================")
            sleep(SLEEP)
            break
        else:
            print(error_code)
            sleep(SLEEP)
            print(" ")


def main():
    while True:
        print("======================================================================")
        x = input(color.BOLD+"Type 'roll' to roll the dice, or type 'exit' to exit this script: "+color.END).lower()
        if x == "roll":
            return sub_main()

        elif x == "exit":
            print("======================================================================")
            sleep(SLEEP)
            break

        else:
            print(error_code)
            sleep(SLEEP)
            print(" ")

main()

# Programmed by: Mubashir Ahmed OR known as Mubashir78 on GitHub
# https://www.github.com/Mubashir78
