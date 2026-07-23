import pyperclip
import PySide6
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
import sys

print("Hello world!")
s = "pyperclip rocks!"
print(PySide6.__version__)
print(sys.winver)
# pyperclip.copy(s)
# content = pyperclip.paste()
# print("content: " + content)

def button_response():
    print("✅ button clicked! ✅")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CopyCatClip")

        # Create container to hold content (buttons, labels, text boxes, etc.)
        main_container = QWidget()
        self.setCentralWidget(main_container)

        container_layout = QVBoxLayout()

        # Create a layout to determine positioning of items in container
        top_container = QWidget()
        layout1 = QVBoxLayout(top_container)

        # Create elements to store in layout/container (buttons, labels, text boxes, etc.)
        label1 = QLabel("One")
        label1.setAlignment(Qt.AlignCenter)
        label2 = QLabel("Two")
        label2.setAlignment(Qt.AlignCenter)
        label3 = QLabel("Three")
        label3.setAlignment(Qt.AlignCenter)

        # Add elements to the layout
        layout1.addWidget(label1)
        layout1.addWidget(label2)
        layout1.addWidget(label3)

        bottom_container = QWidget()
        layout2 = QHBoxLayout(bottom_container)

        button_a = QPushButton("Button A")
        button_b = QPushButton("Button B")
        button_c = QPushButton("Button C")
        layout2.addWidget(button_a)
        layout2.addWidget(button_b)
        layout2.addWidget(button_c)

        container_layout.addWidget(top_container)
        container_layout.addWidget(bottom_container)
        main_container.setLayout(container_layout)

# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()