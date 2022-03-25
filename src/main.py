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
        for spot in command_list:
            current_command = spot.split(' ')

            process_input(current_command)
            

        #taking input
        command_list = read_input()
        #allow time to alt tab back in
        sleep(3)

main()


print('normal termination')