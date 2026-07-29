from PySide6.QtWidgets import QCheckBox, QPlainTextEdit, QPushButton


DEFAULT_PROMPT = "CHANGE THIS TEXT TO THE DESIRED PROMPT."
PLACEHOLDER_TEXT = "Type the desired prompt here."
COPY_STRING = "Copy"
DELETE_STRING = "Delete"

class Prompt:
    def __init__(self):
        """
        Every Prompt has
        (1) A string that is the text for the prompt 
        (2) A QPlainTextEdit object (a text box) to display the string
        (3) "Copy" button
        (4) "Delete" button
        (5) Lock toggle
        """
        print("🚀 creating prompt object")

        # self.prompt_text = ""
        self.prompt_text = DEFAULT_PROMPT
        self.prompt_text_box = QPlainTextEdit()
        self.prompt_text_box.setPlaceholderText(PLACEHOLDER_TEXT)
        self.copy_button = QPushButton(COPY_STRING)
        self.delete_button = QPushButton(DELETE_STRING)
        self.lock_toggle = QCheckBox()

        # Connect buttons to functionality
        self.copy_button.clicked.connect(self.copy_prompt)
        self.delete_button.clicked.connect(self.delete_prompt)
        self.lock_toggle.clicked.connect(self.lock_unlock_prompt)

    def copy_prompt(self):
        print(f"📋✅ Prompt {self.prompt_text} copied to clipboard. ✅📋")

    def delete_prompt(self):
        print(f"📋❌ Prompt {self.prompt_text} delete button clicked ❌📋")
        # Only delete a PromptCollection if there is more than 1 PromptCollection that exists
        '''
        if len(self.list_of_prompts) > 1:
            self.list_of_prompts.remove(self.prompt_text)
            print(f"❌ prompt {self.prompt_text} deleted from collection ❌")
        else:
            print("A minimum of 1 Prompt Collection is required at all times. To delete this Prompt Collection, "
                  "add/create a new Prompt Collection.")
        '''

    def lock_unlock_prompt(self):
        """
        A state of "Checked" == Locked (prompt CANNOT be modified)
        A state of "Unchecked" == Unlocked (prompt CAN be modified)
        :return:
        """
        if self.lock_toggle.isChecked():
            print(f"🔒 Prompt '{self.prompt_text}' locked 🔒")
        else:
            print(f"🔑 Prompt '{self.prompt_text}' unlocked 🔑")