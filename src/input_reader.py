from moves import *

#read in an input string
def read_input():
    commands = input()
    return commands.split(',')

#converts frames to time for sleeping
def convert_time(frames):
    return frames / 60

#loop to delete new line chars I accidentally input sometimes
def fix_new_lines(command):
    for spot in command:
        index = command.index(spot)
        if spot == '\n':
            del command[index]
        elif ('\n' in spot):
            command[index] = command[index].replace('\n', '')
    
    if('\n' in command[0]):
        fix_new_lines(command)

#loop to delete the spaces I accidentally input sometimes
def fix_spaces(command):
    for spot in command:
        if spot == '' or spot == ' ':
            index = command.index(spot)
            del command[index]

    if(command[0] == ''):
        fix_spaces(command)


def loop_input(command_list):
    for spot in command_list:
        current_command = spot.split(' ')

        process_input(current_command)


#main method to process input commands and the directions a user inputs
def process_input(command):
    #since I like to misinput commands here is a VERY hacky fix to replace empty spaces in front of lines...
    fix_new_lines(command)
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
    elif direction == 'wur' or direction == 'wul' or direction == 'wdr' or direction == 'wul':
        walk_diagonal(direction, amount)
    #jumping
    elif direction == 'ju' or direction == 'jr' or direction == 'jl':
        jump(direction, amount)
    #hold in place
    elif direction == "h":
        time.sleep(amount)
    #up or down dash
    elif direction == 'dau' or direction == 'dad':
        dash_up_down(direction, amount)
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
