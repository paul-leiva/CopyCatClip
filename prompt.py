import pyperclip
from PySide6.QtWidgets import QCheckBox, QPlainTextEdit, QPushButton


DEFAULT_PROMPT = ""
PLACEHOLDER_TEXT = "Type the desired prompt here."
COPY_STRING = "📋 Copy"
DELETE_STRING = "❌ Delete"

class Prompt:
    def __init__(self, prompt_text=None, on_delete=None):
        """
        Every Prompt has
        (1) A QPlainTextEdit object (a text box) to display the string
        (2) "Copy" button
        (3) "Delete" button
        (4) Lock toggle
        (5) A container widget
        (6) on_delete action
        """
        print("🚀 creating prompt object")

        if prompt_text:
            print("loading from memory")
        else:
            print("NOT loading from memory")

        self.prompt_text_box = QPlainTextEdit()
        self.prompt_text_box.setPlaceholderText(PLACEHOLDER_TEXT)
        self.prompt_text_box.setFixedHeight(75)

        # Set the plain text in the text box if text is passed in
        if prompt_text:
            self.prompt_text_box.setPlainText(prompt_text)

        self.copy_button = QPushButton(COPY_STRING)
        self.delete_button = QPushButton(DELETE_STRING)
        self.lock_toggle = QCheckBox()

        self.on_delete = on_delete
        self.container_widget = None # Set later by PromptCollection

        # Connect buttons to functionality
        self.copy_button.clicked.connect(self.copy_prompt)
        self.delete_button.clicked.connect(self.delete_prompt)
        self.lock_toggle.clicked.connect(self.lock_unlock_prompt)

    def copy_prompt(self):
        print(f"📋✅ Prompt {self.prompt_text_box.toPlainText()} copied to clipboard. ✅📋")
        pyperclip.copy(self.prompt_text_box.toPlainText())

    def delete_prompt(self):
        print(f"📋❌ Prompt {self.prompt_text_box.toPlainText()} delete button clicked ❌📋")
        if self.on_delete:
            self.on_delete(self)


    def lock_unlock_prompt(self):
        """
        A state of "Checked" == Locked (prompt CANNOT be modified)
        A state of "Unchecked" == Unlocked (prompt CAN be modified)
        :return:
        """
        if self.lock_toggle.isChecked():
            print(f"🔒 Prompt '{self.prompt_text_box.toPlainText()}' locked 🔒")
            self.prompt_text_box.setReadOnly(True)
        else:
            print(f"🔑 Prompt '{self.prompt_text_box.toPlainText()}' unlocked 🔑")
            self.prompt_text_box.setReadOnly(False)