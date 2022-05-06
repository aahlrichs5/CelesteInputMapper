from input_reader import *
from moves import *


def main():
    #priming input
    command_list = read_input()

    #allow time to alt tab back in
    sleep(3)

    #while taking input
    while command_list[0] != 'q':
        #loop through commands
        loop_input(command_list)
            

        #taking input
        command_list = read_input()
        #allow time to alt tab back in
        sleep(3)

main()


print('normal termination')