import pyperclip
import PySide6
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot
import sys

def button_response():
    print("✅ button clicked! ✅")

print("Hello world!")
s = "Python rocks!"
print(PySide6.__version__)
print(sys.winver)

button_numbers = [1, 2, 3, 4]

# Start the app
app = QApplication(sys.argv)

# Create Form
form = QDialog()
form.setWindowTitle("CopyCatClip")

label = QLabel("Hello, World!")
label.show()
sample_button = QPushButton("Sample Button")
sample_button.clicked.connect(button_response)
sample_button.show()

# Create layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(sample_button)
for bn in button_numbers:
    button = QPushButton("Button " + str(bn))
    button.clicked.connect(button_response)
    button.show()
    layout.addWidget(button)
form.setLayout(layout)
form.show()
app.exec()

# pyperclip.copy(s)
# content = pyperclip.paste()
# print("content: " + content)