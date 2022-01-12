from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

#walk inputs
def walk(direction, amount):
    if direction == 'wr':
        keyboard.press('d')
        time.sleep(amount)
        keyboard.release('d')
    elif direction =='wl':
        keyboard.press('a')
        time.sleep(amount)
        keyboard.release('a')
    elif direction =='wd':
        keyboard.press('s')
        time.sleep(amount)
        keyboard.release('s')
    elif direction == 'wu':
        keyboard.press('w')
        time.sleep(amount)
        keyboard.release('w')

def jump(direction, amount):
    if direction == "ju":
        keyboard.press('w')
        keyboard.press('c')
        time.sleep(amount)
        keyboard.release('w')
        keyboard.release('c')
    elif direction == "jr":
        keyboard.press('d')
        keyboard.press('c')
        time.sleep(amount)
        keyboard.release('d')
        keyboard.release('c')
    elif direction == "jl":
        keyboard.press('a')
        keyboard.press('c')
        time.sleep(amount)
        keyboard.release('a')
        keyboard.release('c')

#grab a wall
def grab_wall():
    keyboard.press('z')

#release hold on a wall
def release_wall():
    keyboard.release('z')
    

#dash right inputs
def dash_right(direction, amount):
    if direction == "dal":
        keyboard.press('d')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('d')
        keyboard.release('x')
    elif direction == "daur":
        keyboard.press('d')
        keyboard.press('w')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('d')
        keyboard.release('w')
        keyboard.release('x')
    elif direction == "dadr":
        keyboard.press('d')
        keyboard.press('s')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('d')
        keyboard.release('s')
        keyboard.release('x')

#dash left inputs
def dash_left(direction, amount):
    if direction == 'dal':
        keyboard.press('a')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('a')
        keyboard.release('x')
    elif direction == "daul":
        keyboard.press('a')
        keyboard.press('w')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('a')
        keyboard.release('w')
        keyboard.release('x')
    elif direction == "dadl":
        keyboard.press('a')
        keyboard.press('s')
        keyboard.press('x')
        time.sleep(amount)
        keyboard.release('a')
        keyboard.release('s')
        keyboard.release('x')

#menu and dialog key commands
def press_c():
    keyboard.press('c')
    time.sleep(0.5)
    keyboard.release('c')

def press_x():
    keyboard.press('x')
    time.sleep(0.5)
    keyboard.release('x')

def press_up():
    keyboard.press(keyboard._Key.up)
    time.sleep(0.25)
    keyboard.release(keyboard._Key.up)

def press_down():
    keyboard.press(keyboard._Key.down)
    time.sleep(0.25)
    keyboard.release(keyboard._Key.down)

def skip_dialogue():
    keyboard.press(keyboard._Key.esc)
    time.sleep(0.5)
    keyboard.release(keyboard._Key.esc)
    press_down()
    press_c()


#retry
def retry():
    keyboard.press(keyboard._Key.f3)
    time.sleep(0.75)
    keyboard.release(keyboard._Key.f3)

#restart chapter
def restart():
    keyboard.press('r')
    time.sleep(0.25)
    press_c()

def go_to_map():
    keyboard.press(keyboard._Key.esc)
    time.sleep(0.5)
    keyboard.release(keyboard._Key.esc)
    press_up()
    time.sleep(0.75)
    press_c()
    time.sleep(0.25)
    press_c()

def save_and_quit():
    keyboard.press(keyboard._Key.esc)
    time.sleep(0.5)
    keyboard.release(keyboard._Key.esc)
    press_up()
    time.sleep(0.25)
    press_up()
    time.sleep(0.25)
    press_up()
    time.sleep(0.25)
    press_c()
