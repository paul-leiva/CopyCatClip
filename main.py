import pyperclip
import PySide6, sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from prompt_collection import PromptCollection
from prompt import Prompt

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
    QHBoxLayout {
        border: 2px solid green;
    }
    """
    )

LOCK_ALL_BUTTON_TEXT = "Lock All"
UNLOCK_ALL_BUTTON_TEXT = "Unlock All"

prompt_collection_list = [] # List to hold PromptCollections

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
        main_container_layout = QHBoxLayout(main_container)

        # Create a layout to determine positioning of items in container
        left_container = QWidget()

        # Set layout of container to vertical box layout
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

        # Create right-side container to hole lock/unlock buttons, and list of prompts
        right_container = QWidget()

        # Set layout of container to vertical box layout
        right_layout = QVBoxLayout(right_container)

        # Create "Unlock All" and "Lock All" buttons
        lock_all_button = QPushButton(LOCK_ALL_BUTTON_TEXT)
        lock_all_button.clicked.connect(self.lock_all_prompts)
        unlock_all_button = QPushButton(UNLOCK_ALL_BUTTON_TEXT)
        unlock_all_button.clicked.connect(self.unlock_all_prompts)

        # Create HBox layout to store buttons at top of container
        lock_unlock_layout = QHBoxLayout()
        lock_unlock_layout.addWidget(lock_all_button)
        lock_unlock_layout.addWidget(unlock_all_button)

        # Create widget and add to right_container
        lock_unlock_widget = QWidget()
        lock_unlock_widget.setLayout(lock_unlock_layout)
        right_layout.addWidget(lock_unlock_widget)

        # Make a collection of Mock prompts (dummy data)
        self.mock_prompt_list = []
        for i in range(25):
            self.mock_prompt_list.append(Prompt())
        self.mock_scroll_area = QScrollArea()
        self.mock_widget = QWidget()
        self.mock_vbox = QVBoxLayout()

        for i in range(len(self.mock_prompt_list)):
            self.mock_prompt_list[i].prompt_text = "Mock Prompt " + str(i)
            self.mock_prompt_list[i].prompt_text_box.setPlainText(self.mock_prompt_list[i].prompt_text)

            single_prompt_widget = QWidget()
            single_prompt_layout = QHBoxLayout()

            for x in [self.mock_prompt_list[i].prompt_text_box, self.mock_prompt_list[i].copy_button,
                      self.mock_prompt_list[i].delete_button, self.mock_prompt_list[i].lock_toggle]:
                single_prompt_layout.addWidget(x)

            single_prompt_widget.setLayout(single_prompt_layout)
            self.mock_vbox.addWidget(single_prompt_widget)

        self.mock_widget.setLayout(self.mock_vbox)
        self.mock_scroll_area.setWidget(self.mock_widget)
        self.mock_scroll_area.setWidgetResizable(True)
        right_layout.addWidget(self.mock_scroll_area)

        # Set maximum width of left_container
        left_container.setMaximumWidth(300)

        main_container_layout.addWidget(left_container)
        main_container_layout.addWidget(right_container)
        main_container.setLayout(main_container_layout)

    def lock_all_prompts(self):
        print("🔒🔒🔒 All Prompts LOCKED 🔒🔒🔒")

    def unlock_all_prompts(self):
        print("🔑🔑🔑 All Prompts UNLOCKED 🔑🔑🔑")

# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()