 
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import * 
from tkinter import filedialog
import pyperclip
import sys
import tkinter
import win32gui

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

        # input textbox
        self.input_box = QTextEdit(self)
        self.input_box.move(20, 25)
        self.input_box.resize(350, 600)
        self.input_box.setLineWrapColumnOrWidth(350)

        # open a txt file
        self.input_file_button = QPushButton("Open Text File", self)
        self.input_file_button.move(400, 25)
        self.input_file_button.clicked.connect(self.open_file_explorer)

        # save a txt file
        self.input_file_button = QPushButton("Save Text File", self)
        self.input_file_button.move(400, 75)
        self.input_file_button.clicked.connect(self.save_file)

        self.dialog_label = QLabel("", self)
        self.dialog_label.move(375, 125)
        self.dialog_label.resize(145, 360)
        self.dialog_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.dialog_label.setWordWrap(True)

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

    Files = [('Text Document', '*.txt'),
			        ('Markdown File', '*.md'),
                    ('All Files', '*.*')] 

    # helper funtions
    def open_file_explorer(self):
        self.clear_dialog_label()
        root = tkinter.Tk()
        root.withdraw()

        try: 
            input_file = open(filedialog.askopenfilename(filetypes = self.Files, defaultextension = self.Files), 'r')
            input = input_file.read()
            self.fill_input_box(self, input)
            input_file.close()
        except:
            self.dialog_label.setText("Did not open file or there was a problem opening the file")

    def save_file(self):
        self.clear_dialog_label()
        root = tkinter.Tk()
        root.withdraw()

        text = self.input_box.toPlainText()

        try:
            text_file = open(filedialog.asksaveasfilename(filetypes = self.Files, defaultextension = self.Files), 'w')
            text_file.write(text)
            text_file.close()
        except:
            self.dialog_label.setText("Did not save file or there was a problem saving the file")

    def fill_input_box(self, window, input):
        self.clear_dialog_label()
        self.input_box.clear()
        try:
            self.input_box.setPlainText(input)
        except:
            self.dialog_label.setText("Did not open file or there was a problem opening the file")

    def clear_input_box(self):
        self.dialog_label.setText("Text cleared")

    def copy_input_box(self):
        input = self.input_box.toPlainText()
        pyperclip.copy(input)
        self.dialog_label.setText("Text copied to clipboard")

    def confirm_button_clicked(self):
        try:
            self.focus_celeste()
        except:
            self.dialog_label.setText("Was not able to focus Celeste")
            return;

        input = self.input_box.toPlainText()
        input = input.split(',')
        try:
            self.dialog_label.setText("Executing commands...")
            loop_input(input)
        except:
            self.dialog_label.setText("Was unable to process input")

    def focus_celeste(self):
        self.clear_dialog_label()
        window = win32gui.FindWindow(None, "Celeste")
        win32gui.SetForegroundWindow(window)

    def clear_dialog_label(self):
        self.dialog_label.setText("")
  

# create pyqt6 app
App = QApplication(sys.argv)
  
# create the instance of Window
window = Window()
  
# start the app
sys.exit(App.exec())