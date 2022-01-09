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
    while direction != 'quit' or amount == -1:
        #retry options
        if direction == 'retry':
            retry()
        elif direction == 'restart':
            restart()
        elif direction == 'map':
            go_to_map()
        elif direction == 'save':
            save_and_quit()
        #walking
        elif direction == 'wr' or direction == 'wl' or direction == 'wd' or direction == 'wu':
            walk(direction, amount)
        #jumping
        elif direction == 'ju' or direction == 'jr' or direction == 'jl':
            jump(direction, amount)
        #hold in place
        elif direction == "h":
            time.sleep(amount)
        #right dashes
        elif direction == 'dar' or direction == "daur" or direction == "dadr":
            dash_right(direction, amount)
        #left dashes
        elif direction == 'dal' or direction == "daul" or direction == "dadl":
            dash_left(direction, amount)
        #hold and release wall
        elif direction == 'gw':
            grab_wall()
        elif direction == "rw":
            release_wall()


    #taking input
        direction, amount = input().split()
        amount = float(amount)
        time.sleep(3)

main()


print('normal termination')