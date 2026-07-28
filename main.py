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

stylesheet = (
    """
    QMainWindow { 
        border: 2px solid red; 
    }
    
    QScrollArea { 
        border: 2px solid blue; 
    }
    """
    )

def button_response():
    print("✅ button clicked! ✅")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CopyCatClip")

        # Create container to hold content (buttons, labels, text boxes, etc.)
        main_container = QWidget()
        app.setStyleSheet(stylesheet)
        self.setCentralWidget(main_container)

        # Container to hold
        container_layout = QHBoxLayout(main_container)

        # Create a layout to determine positioning of items in container
        left_container = QWidget()

        # Apply layout to parent container (left_container
        left_layout = QVBoxLayout(left_container)

        # Create button to store the current prompt collection that is selected
        selected_prompt_collection = QPushButton("Selected Prompt Collection")
        left_layout.addWidget(selected_prompt_collection)

        prompt_collection_label = QLabel("Prompt Collections")
        prompt_collection_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(prompt_collection_label)

        # Create scrollable panel of prompt collections
        prompts_scroll_area = QScrollArea()
        prompts_widget = QWidget()
        prompts_layout = QVBoxLayout()
        prompt_collection_buttons = []
        for i in range(5):
            pc_button = QPushButton(f"Prompts {i}")
            pc_button.clicked.connect(button_response)
            prompts_layout.addWidget(pc_button)
            prompt_collection_buttons.append(pc_button)

        prompts_widget.setLayout(prompts_layout)

        prompts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        prompts_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        prompts_scroll_area.setWidgetResizable(True)
        prompts_scroll_area.setWidget(prompts_widget)
        left_layout.addWidget(prompts_scroll_area)

        # Button for Creating/Adding a new collection
        add_collection_button = QPushButton("➕ Add New Collection")
        add_collection_button.clicked.connect(button_response)
        left_layout.addWidget(add_collection_button)

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        layout3 = QVBoxLayout()

        scrollable_buttons = []
        for i in range(10):
            button = QPushButton(f"Button {i}")
            button.clicked.connect(button_response)
            layout3.addWidget(button)
            scrollable_buttons.append(button)

        scroll_widget.setLayout(layout3)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        container_layout.addWidget(left_container)
        container_layout.addWidget(scroll_area)
        main_container.setLayout(container_layout)

# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()