from PySide6.QtWidgets import QHBoxLayout, QWidget
from prompt import Prompt
from prompt_collection import PromptCollection


class ClipboardHistory(PromptCollection):
    def __init__(self, collection_title=None, collection_prompts=None):
        super().__init__(collection_title, collection_prompts=[])
        self.make_scroll_area()

    def make_widget_for_single_prompt(self, clipboard_text):
        # Make a Prompt from the clipboard_text
        prompt = Prompt(clipboard_text)

        single_prompt_widget = QWidget()
        single_prompt_layout = QHBoxLayout()

        for x in [prompt.prompt_text_box, prompt.copy_button]:
            single_prompt_layout.addWidget(x)

        single_prompt_widget.setLayout(single_prompt_layout)
        prompt.container_widget = single_prompt_widget  # <-- Assign the wrapper
        return single_prompt_widget

    def make_scroll_area(self):
        self.prompts_widget.setLayout(self.vbox_layout)
        self.scroll_area.setWidget(self.prompts_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setProperty("class", "scroll_area")