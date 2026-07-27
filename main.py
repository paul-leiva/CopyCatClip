import pyperclip
import PySide6
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
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
        button_a.clicked.connect(button_response)
        button_b = QPushButton("Button B")
        button_b.clicked.connect(button_response)
        button_c = QPushButton("Button C")
        button_c.clicked.connect(button_response)
        layout2.addWidget(button_a)
        layout2.addWidget(button_b)
        layout2.addWidget(button_c)

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        layout3 = QVBoxLayout()

        scrollable_buttons = []
        for i in range(2):
            button = QPushButton(f"Button {i}")
            button.clicked.connect(button_response)
            layout3.addWidget(button)
            scrollable_buttons.append(button)

        scroll_widget.setLayout(layout3)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        container_layout.addWidget(top_container)
        container_layout.addWidget(bottom_container)
        container_layout.addWidget(scroll_area)
        main_container.setLayout(container_layout)

# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()