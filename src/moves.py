from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

#walk inputs
def walk(direction, amount):
    if direction == 'wr':
        keyboard.press('d')
        time.sleep(amount)
        keyboard.release('d')
    else:
        keyboard.press('a')
        time.sleep(amount)
        keyboard.release('a')

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


