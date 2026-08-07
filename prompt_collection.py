from prompt import Prompt
from PySide6.QtWidgets import QHBoxLayout, QMessageBox, QPushButton, QScrollArea, QVBoxLayout, QWidget


DEFAULT_COLLECTION_NAME = "PROMPT COLLECTION NAME"
ADD_PROMPT_BUTTON_TEXT = "➕ Add Prompt"
DELETE_PROMPT_ERROR_MESSAGE = ("Unable to delete Prompt. A minimum of 1 Prompt is required at all times. "
                               "If you would like to delete all Prompts shown, delete the Prompt Collection.")

class PromptCollection:
    def __init__(self, collection_title=None, collection_prompts=None):
        """
        Every Prompt Collection has
        (1) A title of the prompt collection
        (2) A list of Prompt objects
        (3) A button to add a prompt
        (4) A button to access the PromptCollection
        
        The list of Prompt objects will NEVER be empty
        """

        print("Creating prompt collection")

        if collection_title:
            self.title = collection_title
        else:
            self.title = DEFAULT_COLLECTION_NAME
        if collection_prompts:
            self.list_of_prompts = [Prompt(cp, on_delete=self.delete_prompt_from_collection)
                                    for cp in collection_prompts]
        else:
            # self.list_of_prompts = [Prompt()]
            self.list_of_prompts = [Prompt(on_delete=self.delete_prompt_from_collection)]
        self.add_prompt_button = QPushButton(ADD_PROMPT_BUTTON_TEXT)
        self.add_prompt_button.clicked.connect(self.add_prompt_to_collection)

        self.prompt_collection_button = QPushButton(self.title)

        # Form the widget/scroll area for the prompts
        self.scroll_area = QScrollArea()
        self.prompts_widget = QWidget()
        self.vbox_layout = QVBoxLayout()

        self.make_scroll_area()

        print("prompt_collection: " + str(self))

        for p in self.list_of_prompts:
            print("prompt_text: " + p.prompt_text)

    def add_prompt_to_collection(self):
        print(f"✅ prompt added to collection ✅")
        new_prompt = Prompt(on_delete=self.delete_prompt_from_collection)
        self.list_of_prompts.append(new_prompt)

        # Update the UI (layouts, scroll area for PromptCollection object)
        self.vbox_layout.removeWidget(self.add_prompt_button)
        new_widget = self.make_widget_for_single_prompt(new_prompt)
        self.vbox_layout.addWidget(new_widget)
        self.vbox_layout.addWidget(self.add_prompt_button)


    def delete_prompt_from_collection(self, prompt_to_delete):
        print(f"❌ prompt {"plainText"} deleted from collection ❌")
        if self.vbox_layout.count() == 2:
            QMessageBox.critical(None, "Only one Prompt left!", DELETE_PROMPT_ERROR_MESSAGE)
            return

        self.list_of_prompts.remove(prompt_to_delete)
        widget = prompt_to_delete.container_widget
        self.vbox_layout.removeWidget(widget)
        widget.setParent(None)
        widget.deleteLater()


    def delete_prompt_collection(self, prompt_collection_to_delete):
        # Only delete a PromptCollection if there is more than 1 PromptCollection that exists
        if len(self.list_of_prompts) > 1:
            self.list_of_prompts.remove(prompt_collection_to_delete)
            print(f"❌ prompt {prompt_collection_to_delete.prompt_text} deleted from collection ❌")
        else:
            print("A minimum of 1 Prompt Collection is required at all times. To delete this Prompt Collection, "
                  "add/create a new Prompt Collection.")

    def make_widget_for_single_prompt(self, prompt):
        single_prompt_widget = QWidget()
        single_prompt_layout = QHBoxLayout()

        for x in [prompt.prompt_text_box, prompt.copy_button,
                  prompt.delete_button, prompt.lock_toggle]:
            single_prompt_layout.addWidget(x)

        single_prompt_widget.setLayout(single_prompt_layout)
        prompt.container_widget = single_prompt_widget  # <-- Assign the wrapper
        return single_prompt_widget

    def make_scroll_area(self):
        for prompt in self.list_of_prompts:
            single_prompt_widget = self.make_widget_for_single_prompt(prompt)
            self.vbox_layout.addWidget(single_prompt_widget)

        self.vbox_layout.addWidget(self.add_prompt_button)
        self.prompts_widget.setLayout(self.vbox_layout)
        self.scroll_area.setWidget(self.prompts_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setProperty("class", "scroll_area")
