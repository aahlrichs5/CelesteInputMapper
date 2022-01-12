from moves import *

#read in an input string
def read_input():
    commands = input()
    return commands.split(',')

#process the string to return the current command
def process_single_command(single_command):
    return single_command.split(' ')

#converts frames to time for sleeping
def convert_time(frames):
    return frames / 60

#loop to delete the spaces I accidentally input sometimes
def fix_spaces(command):
    for spaces in command:
        if command[0] == '':
            del command[0]


#main method to process input commands and the directions a user inputs
def process_input(command):

    #since I like to misinput commands here is a hacky fix to replace empty spaces in front of lines...
    if command[0] == '':
        fix_spaces(command)

    direction = command [0]

    #default amount is 30 frames
    if(len(command) == 2):
        amount = command[1]
    else:
        amount = 30
    amount = float(amount)
    amount = convert_time(amount)

    
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
    #menu and dialog navigation presses
    elif direction == 'skip':
        skip_dialogue()
    elif direction == 'c':
        press_c()
    elif direction == 'x':
        press_x()
    elif direction == 'up':
        press_up()
    elif direction == 'down':
        press_down()
    else:
        print("Command not recognized: ")
        print(command)
