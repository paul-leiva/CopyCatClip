from PySide6.QtWidgets import QPushButton
from prompt import Prompt


DEFAULT_COLLECTION_NAME = "PROMPT COLLECTION NAME"
ADD_PROMPT_BUTTON_TEXT = "➕ Add Prompt"

class PromptCollection:
    def __init__(self):
        """
        Every Prompt Collection has
        (1) A title of the prompt collection
        (2) A list of Prompt objects
        (3) A button to add a prompt
        
        The list of Prompt objects will NEVER be empty
        """

        print("Creating prompt collection")

        self.title = DEFAULT_COLLECTION_NAME
        self.list_of_prompts = [Prompt()]
        self.add_prompt_button = QPushButton(ADD_PROMPT_BUTTON_TEXT)
        self.add_prompt_button.clicked.connect(self.add_prompt_to_collection)

        print("prompt_collection: " + str(self))

        for p in self.list_of_prompts:
            print("prompt_text: " + p.prompt_text)

    def add_prompt_to_collection(self):
        print(f"✅ prompt added to collection ✅")
        self.list_of_prompts.append(Prompt())

    def delete_prompt_from_collection(self, prompt_to_delete: Prompt):
        print(f"❌ prompt {prompt_to_delete.prompt_text} deleted from collection ❌")

    def delete_prompt_collection(self, prompt_collection_to_delete):
        # Only delete a PromptCollection if there is more than 1 PromptCollection that exists
        if len(self.list_of_prompts) > 1:
            self.list_of_prompts.remove(prompt_collection_to_delete)
            print(f"❌ prompt {prompt_collection_to_delete.prompt_text} deleted from collection ❌")
        else:
            print("A minimum of 1 Prompt Collection is required at all times. To delete this Prompt Collection, "
                  "add/create a new Prompt Collection.")