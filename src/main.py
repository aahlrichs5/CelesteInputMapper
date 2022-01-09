from pynput.keyboard import Key, Controller
import time

from moves import *

keyboard = Controller()

def main():
    #priming input
    direction, amount = input().split()
    amount = float (amount)
    time.sleep(3)

    #while taking input
    while direction != 'z' or amount == -1:
        #walking
        if direction == 'wr' or direction == 'wl':
            walk(direction, amount)
        #hold in place
        elif direction == "h":
            time.sleep(amount)
        #right dashes
        elif direction == 'dar' or direction == "daur" or direction == "dadr":
            dash_right(direction, amount)
        #left dashes
        elif direction == 'dal' or direction == "daul" or direction == "dadl":
            dash_left(direction, amount)


    #taking input
        direction, amount = input().split()
        amount = float(amount)
        time.sleep(3)

main()


print('normal termination')