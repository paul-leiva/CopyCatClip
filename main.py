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

'''
@staticmethod
def add_prompt_button_clicked():
    print("✅✅ Add Prompt Button Clicked ✅✅")
    n = len(self.mock_prompt_list)
    self.mock_prompt_list[n - 1].prompt_text = "Mock Prompt " + str(n - 1)
    self.mock_prompt_list[n - 1].prompt_text_box.setPlainText(self.mock_prompt_list[n - 1].prompt_text)

    single_prompt_widget = QWidget()
    single_prompt_layout = QHBoxLayout()

    for x in [self.mock_prompt_list[n - 1].prompt_text_box, self.mock_prompt_list[n - 1].copy_button,
              self.mock_prompt_list[n - 1].delete_button, self.mock_prompt_list[n - 1].lock_toggle]:
        single_prompt_layout.addWidget(x)

    single_prompt_widget.setLayout(single_prompt_layout)
    self.mock_vbox.addWidget(single_prompt_widget)
'''


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CopyCatClip")

        # Form initial data to make PromptCollection objects from memory
        with open("memory.txt") as mem:
            for pc in mem:
                print("Next Prompt Collection: " + pc)
                data = pc.split(", ")

                # Use the initial String as the PromptCollection's title
                prompt_collection_title = data[0]

                # Use all other remaining strings as the text for each Prompt
                prompt_collection_prompt_texts = []
                for x in data[1:-1]:
                    print("x: " + str(x))
                    prompt_collection_prompt_texts.append(x)

                # Remove newline character from last prompt
                prompt_collection_prompt_texts.append(data[-1].rstrip("\n"))

                # Construct a PromptCollection object with the data from memory
                prompt_collection_list.append(
                    PromptCollection(prompt_collection_title, prompt_collection_prompt_texts)
                )

        print("*** Initial prompt_collection_list: ***")
        for e in prompt_collection_list:
            print(e.title, end=" | ")
            for x in e.list_of_prompts:
                print(x.prompt_text, end=", ")
            print()

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
        self.selected_prompt_collection = prompt_collection_list[0]
        self.selected_prompt_collection_button = QPushButton(self.selected_prompt_collection.title)
        left_layout.addWidget(self.selected_prompt_collection_button)

        prompt_collection_label = QLabel("Prompt Collections")
        prompt_collection_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(prompt_collection_label)

        # Create scrollable panel of prompt collections
        prompts_scroll_area = QScrollArea()
        prompts_widget = QWidget()
        prompts_layout = QVBoxLayout()
        prompt_collection_buttons = []

        for pc in prompt_collection_list:
            pc_button = QPushButton(pc.title)
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

        # By default, set the right layout to the prompts from the very first PromptCollection object in memory
        right_layout.addWidget(self.selected_prompt_collection.scroll_area)

        # Set maximum width of left_container
        left_container.setMaximumWidth(300)

        main_container_layout.addWidget(left_container)
        main_container_layout.addWidget(right_container)
        main_container.setLayout(main_container_layout)

    def lock_all_prompts(self):
        print("🔒🔒🔒 All Prompts LOCKED 🔒🔒🔒")

    def unlock_all_prompts(self):
        print("🔑🔑🔑 All Prompts UNLOCKED 🔑🔑🔑")

    def add_prompt_button_clicked(self):
        print("✅✅ Add Prompt Button Clicked ✅✅")
        # self.selected_prompt_collection.add_prompt_to_collection()

# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()