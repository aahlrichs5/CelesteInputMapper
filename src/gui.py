 
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtWidgets import * 
import pyperclip
import sys
import tkinter
from tkinter import filedialog

from input_reader import loop_input
  
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title and size of the window
        self.setWindowIcon(QtGui.QIcon('assets\inputmapper.png'))
        self.setWindowTitle("Celeste Input Mapper")
  
        width = 525
        height = 650
        self.setFixedSize(width, height)

        # open a txt file
        self.input_file_button = QPushButton("Open Text File", self)
        self.input_file_button.move(400, 25)
        self.input_file_button.clicked.connect(self.open_file_explorer)

        # save a txt file
        self.input_file_button = QPushButton("Save Text File", self)
        self.input_file_button.move(400, 75)
        self.input_file_button.clicked.connect(self.save_file)

        # input textbox
        self.input_box = QTextEdit(self)
        self.input_box.move(20, 25)
        self.input_box.resize(350, 600)
        self.input_box.setLineWrapColumnOrWidth(350)

        # clear inputs button
        self.clear_button = QPushButton("Clear Inputs", self)
        self.clear_button.move(400, 497)
        self.clear_button.clicked.connect(self.clear_input_box)

        # copy inputs button
        self.copy_button = QPushButton("Copy Text", self)
        self.copy_button.move(400, 547)
        self.copy_button.clicked.connect(self.copy_input_box)

        # confirm inputs button
        self.confirm_button = QPushButton("Confirm Moves", self)
        self.confirm_button.move(400, 597)
        self.confirm_button.clicked.connect(self.confirm_button_clicked)
  
        # show the window
        self.show()
        

    # helper funtions
    def open_file_explorer(self):
        root = tkinter.Tk()
        root.withdraw()

        try: 
            input_file = open(filedialog.askopenfilename(), 'r')
            input = input_file.read()
            self.fill_input_box(self, input)
            input_file.close()
        except:
            print("Was not able to open file")

    def save_file(self):
        root = tkinter.Tk()
        root.withdraw()

        Files = [('Text Document', '*.txt'),
			        ('Markdown File', '*.md'),
                    ('All Files', '*.*')]

        text = self.input_box.toPlainText()

        try:
            text_file = open(filedialog.asksaveasfilename(filetypes = Files, defaultextension = Files), 'w')
            text_file.write(text)
            text_file.close()
        except:
            print("Was not able to save file")

    def fill_input_box(self, window, input):
        self.input_box.clear()
        try:
            self.input_box.setPlainText(input)
        except:
            print("Was not able to open file")

    def clear_input_box(self):
        self.input_box.clear()

    def copy_input_box(self):
        input = self.input_box.toPlainText()
        pyperclip.copy(input)

    def confirm_button_clicked(self):
        input = self.input_box.toPlainText()
        input = input.split(',')
        try:
            loop_input(input)
        except:
            print("Was unable to process input")
  
  
# create pyqt6 app
App = QApplication(sys.argv)
  
# create the instance of Window
window = Window()
  
# start the app
sys.exit(App.exec())