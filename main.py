from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QInputDialog, QLabel, QMainWindow, QMessageBox, QPushButton, QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from prompt_collection import PromptCollection
import sys

stylesheet = (
    """
    QPlainTextEdit {
        border: 2px solid orange;
    }
    QPushButton[id="self.selected_prompt_collection_button"] {
        border: 2px solid blue;
    }
    QScrollArea[class="scroll_area"] { 
        border: 2px solid blue; 
    }
    """
    )

LOCK_ALL_BUTTON_TEXT = "🔒 Lock All"
UNLOCK_ALL_BUTTON_TEXT = "🔑 Unlock All"
ADD_PROMPT_COLLECTION_BUTTON_TEXT = "➕ Add New Prompt Collection"
RENAME_PROMPT_COLLECTION_TEXT = "📝 Rename Prompt Collection"
RENAME_DETAIL_TEXT = "Enter the name for the new Prompt Collection. DO NOT enter a name that is already in use!"
DELETE_PROMPT_COLLECTION_TEXT = "❌ Delete Prompt Collection"
DELETE_DETAIL_TEXT = "Are you sure you want to delete the currently selected Prompt Collection?"
SAVE_AND_CLOSE_WARNING = "Are you sure you want to quit? All prompts will be saved upon quitting."
SELECTED_PROMPT_COLLECTION_INDICATOR = "✅ "

prompt_collection_list = [] # List to hold PromptCollections

def button_response():
    print("✅ button clicked! ✅")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CopyCatClip")

        self.selected_index = 0

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
        self.selected_prompt_collection_button = QPushButton(
            SELECTED_PROMPT_COLLECTION_INDICATOR + prompt_collection_list[self.selected_index].title
        )
        self.selected_prompt_collection_button.setProperty("id", "self.selected_prompt_collection_button")
        left_layout.addWidget(self.selected_prompt_collection_button)

        prompt_collections_label = QLabel("Prompt Collections")
        prompt_collections_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(prompt_collections_label)

        # Create scrollable panel of prompt collections
        self.prompts_scroll_area = QScrollArea()
        self.prompts_widget = QWidget()
        self.prompts_layout = QVBoxLayout()
        self.prompt_collection_buttons = []

        for i, pc in enumerate(prompt_collection_list):
            prompt_collection_list[i].prompt_collection_button.clicked.connect(lambda checked, val=prompt_collection_list[i].prompt_collection_button: self.prompt_collection_button_clicked(val))
            self.prompts_layout.addWidget(prompt_collection_list[i].prompt_collection_button)
            self.prompt_collection_buttons.append(prompt_collection_list[i].prompt_collection_button)

        self.old_button = prompt_collection_list[self.selected_index].prompt_collection_button
        self.old_button.setText(SELECTED_PROMPT_COLLECTION_INDICATOR + prompt_collection_list[self.selected_index].title)
        self.new_button = None

        self.prompts_widget.setLayout(self.prompts_layout)

        self.prompts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.prompts_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prompts_scroll_area.setWidgetResizable(True)
        self.prompts_scroll_area.setWidget(self.prompts_widget)
        left_layout.addWidget(self.prompts_scroll_area)

        # Button for Creating/Adding a new PromptCollection
        add_collection_button = QPushButton(ADD_PROMPT_COLLECTION_BUTTON_TEXT)
        add_collection_button.clicked.connect(self.add_prompt_collection_button_clicked)
        left_layout.addWidget(add_collection_button)

        # Create right-side container to hole lock/unlock buttons, and list of prompts
        right_container = QWidget()

        # Set layout of container to vertical box layout
        self.right_layout = QVBoxLayout(right_container)

        # Create "Unlock All" and "Lock All" buttons
        lock_all_button = QPushButton(LOCK_ALL_BUTTON_TEXT)
        lock_all_button.clicked.connect(self.lock_all_prompts)
        unlock_all_button = QPushButton(UNLOCK_ALL_BUTTON_TEXT)
        unlock_all_button.clicked.connect(self.unlock_all_prompts)

        # Create VBox layout to store "Lock All" and "Unlock All" buttons at top of container
        lock_unlock_layout = QVBoxLayout()
        lock_unlock_layout.addWidget(lock_all_button)
        lock_unlock_layout.addWidget(unlock_all_button)
        # Nest "Lock All" and "Unlock All" buttons in widget
        lock_unlock_widget = QWidget()

        # Create "Rename Prompt Collection" and "Delete Prompt Collection" buttons
        rename_prompt_collection_button = QPushButton(RENAME_PROMPT_COLLECTION_TEXT)
        rename_prompt_collection_button.clicked.connect(self.rename_prompt_collection_button_clicked)
        delete_prompt_collection_button = QPushButton(DELETE_PROMPT_COLLECTION_TEXT)
        delete_prompt_collection_button.clicked.connect(self.delete_prompt_collection_button_clicked)

        # Create VBox layout to store buttons to modify/delete buttons at top of container
        rename_delete_layout = QVBoxLayout()
        rename_delete_layout.addWidget(rename_prompt_collection_button)
        rename_delete_layout.addWidget(delete_prompt_collection_button)
        rename_delete_widget = QWidget()

        # Create widgets and add to right_container
        lock_unlock_widget.setLayout(lock_unlock_layout)
        rename_delete_widget.setLayout(rename_delete_layout)

        # Store the two widgets in a QHBoxLayout
        top_button_layout = QHBoxLayout()
        top_button_layout.addWidget(rename_delete_widget)
        top_button_layout.addWidget(lock_unlock_widget)
        top_button_widget = QWidget()
        top_button_widget.setLayout(top_button_layout)

        self.right_layout.addWidget(top_button_widget)

        # By default, set the right layout to the prompts from the very first PromptCollection object in memory
        self.right_layout.addWidget(prompt_collection_list[self.selected_index].scroll_area)

        # Set maximum width of left_container
        left_container.setMaximumWidth(300)

        main_container_layout.addWidget(left_container)
        main_container_layout.addWidget(right_container)
        main_container.setLayout(main_container_layout)

    def prompt_collection_button_clicked(self, button):
        print(f"📧📧 Prompt Collection button clicked:  {button.text()} 📧📧")
        collection_title = button.text()

        if collection_title.startswith(SELECTED_PROMPT_COLLECTION_INDICATOR):
            print("Same Prompt Collection (button) already selected")
            return

        self.old_button.setText(prompt_collection_list[self.selected_index].title)

        for i, pc in enumerate(prompt_collection_list):
            if prompt_collection_list[i].title == collection_title:
                print("now displaying " + str(i) + " | " + pc.title)
                old_widget = prompt_collection_list[self.selected_index].scroll_area
                self.selected_index = i
                self.right_layout.replaceWidget(old_widget, prompt_collection_list[self.selected_index].scroll_area)
                old_widget.setParent(None)
                prompt_collection_list[self.selected_index].prompt_collection_button.setText(
                    SELECTED_PROMPT_COLLECTION_INDICATOR + prompt_collection_list[self.selected_index].title
                )
                self.selected_prompt_collection_button.setText(
                    prompt_collection_list[self.selected_index].prompt_collection_button.text()
                )
                self.old_button = prompt_collection_list[self.selected_index].prompt_collection_button
                break

    def lock_all_prompts(self):
        print("🔒🔒🔒 All Prompts LOCKED 🔒🔒🔒")
        for prompt in prompt_collection_list[self.selected_index].list_of_prompts:
            prompt.lock_toggle.setCheckState(Qt.CheckState.Checked)
            prompt.prompt_text_box.setReadOnly(True)

    def unlock_all_prompts(self):
        print("🔑🔑🔑 All Prompts UNLOCKED 🔑🔑🔑")
        for prompt in prompt_collection_list[self.selected_index].list_of_prompts:
            prompt.lock_toggle.setCheckState(Qt.CheckState.Unchecked)
            prompt.prompt_text_box.setReadOnly(False)

    def add_prompt_collection_button_clicked(self):
        print("💥💥 Add New Prompt Collection button clicked 💥💥")
        prompt_collection_titles = [pc.title for pc in prompt_collection_list]
        print("prompt_collection_titles: " + str(prompt_collection_titles))
        text, result = QInputDialog.getText(self, "Add New Prompt Collection",
                    "Enter the name for the new Prompt Collection. DO NOT enter a name that is already in use!")
        print("text: " + str(text))
        print("result: " + str(result))
        while (text == "" or text in prompt_collection_titles) and result == True:
            QMessageBox.critical(None, "Name already in use!", "Name already in use. Please type a different name for the new Prompt Collection.")
            text, result = QInputDialog.getText(self, "Add New Prompt Collection",
            "Enter the name for the new Prompt Collection. DO NOT enter a name that is already in use!")
            print("text: " + str(text))
            print("result: " + str(result))

        if result:
            print("💯💯 text: " + str(text))
            new_prompt_collection = PromptCollection(text)
            print("new Prompt Collection: " + str(new_prompt_collection.title))
            prompt_collection_list.append(new_prompt_collection)

            # Update UI (list of Prompt Collection buttons and list of PromptCollection objects)
            prompt_collection_list[-1].prompt_collection_button.clicked.connect(
                lambda checked, val=prompt_collection_list[-1].prompt_collection_button: self.prompt_collection_button_clicked(val))
            self.prompts_layout.addWidget(prompt_collection_list[-1].prompt_collection_button)
            self.prompt_collection_buttons.append(prompt_collection_list[-1].prompt_collection_button)

    def delete_prompt_collection_button_clicked(self):
        print(DELETE_PROMPT_COLLECTION_TEXT)

        if len(prompt_collection_list) < 2:
            QMessageBox.critical(None, "Prompt Collection NOT Deleted",
            "There must be at least 2 Prompt Collections to delete a Prompt Collection. Add another Prompt Collection to allow deletion.")
            return

        confirm_delete_window = QMessageBox()
        confirm_delete_window.setWindowTitle(DELETE_PROMPT_COLLECTION_TEXT)
        confirm_delete_window.setText(DELETE_DETAIL_TEXT + "\n\n(" + prompt_collection_list[self.selected_index].title + ")")
        confirm_delete_window.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirm_delete_window.exec()

        if result == QMessageBox.Yes:
            print("Prompt Collection Deleted")

        collection_to_delete = prompt_collection_list[self.selected_index]

        # 1. Remove the collection's button from the left-side list
        button_to_remove = collection_to_delete.prompt_collection_button
        self.prompts_layout.removeWidget(button_to_remove)
        button_to_remove.setParent(None)
        button_to_remove.deleteLater()
        self.prompt_collection_buttons.remove(button_to_remove)

        # 2. Remove the collection's scroll area from the right side
        self.right_layout.removeWidget(collection_to_delete.scroll_area)
        collection_to_delete.scroll_area.setParent(None)

        # 3. Remove the collection itself from the data list
        prompt_collection_list.remove(collection_to_delete)

        # 4. Pick a new selection (fall back to the first remaining collection)
        self.selected_index = min(self.selected_index, len(prompt_collection_list) - 1)
        new_selected = prompt_collection_list[self.selected_index]

        self.old_button = new_selected.prompt_collection_button
        new_selected.prompt_collection_button.setText(
            SELECTED_PROMPT_COLLECTION_INDICATOR + new_selected.title
        )
        self.selected_prompt_collection_button.setText(
            new_selected.prompt_collection_button.text()
        )

        # 5. Show the newly-selected collection's prompts
        self.right_layout.addWidget(new_selected.scroll_area)


    def rename_prompt_collection_button_clicked(self):
        print(RENAME_PROMPT_COLLECTION_TEXT)
        prompt_collection_titles = [pc.title for pc in prompt_collection_list]
        new_title, result = QInputDialog.getText(self, RENAME_PROMPT_COLLECTION_TEXT, RENAME_DETAIL_TEXT)
        while (new_title == "" or new_title in prompt_collection_titles) and result == True:
            QMessageBox.critical(None, RENAME_PROMPT_COLLECTION_TEXT, "Name already in use. Please type a different name for the Prompt Collection.")
            text, result = QInputDialog.getText(self, RENAME_PROMPT_COLLECTION_TEXT,
            "Enter the name for the Prompt Collection. DO NOT enter a name that is already in use!")

        if result:
            prompt_collection_list[self.selected_index].title = new_title
            prompt_collection_list[self.selected_index].prompt_collection_button.setText(
                SELECTED_PROMPT_COLLECTION_INDICATOR + prompt_collection_list[self.selected_index].title
            )
            self.selected_prompt_collection_button.setText(
                prompt_collection_list[self.selected_index].prompt_collection_button.text()
            )

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(
            self, "Quit?", SAVE_AND_CLOSE_WARNING,
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                with open("memory.txt", "w") as mem:
                    for pc in prompt_collection_list:
                        prompt_texts = [p.prompt_text_box.toPlainText() for p in pc.list_of_prompts]
                        line = ", ".join([pc.title] + prompt_texts)
                        mem.write(line + "\n")
            except Exception as e:
                print(f"⚠️ Failed to save: {e}")
            print("Closing...")
            event.accept()
        else:
            event.ignore()


# Start the app
app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 400)
window.show()
app.exec()