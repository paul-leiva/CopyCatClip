# CopyCatClip
CopyCatClip is a desktop application, built with PySide6 (Qt for Python) and the pyperclip module/library, for organizing reusable snippets of text and keeping track of what's recently been copied to your clipboard.

## Purpose

Typing the same prompts, code snippets, or canned responses over and over is tedious. CopyCatClip lets you save them once, organize them into named collections, and copy any of them back to your clipboard with a single click — while also automatically logging what you copy from anywhere else on your system, so that recently-used text is never more than a click away!

## Features

- **Prompt Collections** — Group related snippets of text into named collections (e.g. "Email Templates", "Code Snippets"). Create, rename, and delete Prompt Collections as needed.
- **Manage individual prompts** — Within a Prompt Collection, there is the ability to add new prompts, edit their text, delete ones you no longer need, and lock a prompt to prevent accidental edits.
- **One-click copy** — Every prompt has a Copy button that sends its text straight to your system clipboard.
- **Automatic Clipboard History** — A background listener watches your system clipboard and automatically adds a new entry any time you copy something new, so you can quickly reuse or re-copy recent clipboard content from within the app.
- **Persistence** — Your prompt collections are saved to `memory.txt` when you close the app and reloaded automatically the next time you launch it. (Clipboard history is session-only and is cleared upon closing the program.)

## Video Demo
[![Anti-Trust - War Machine](https://img.youtube.com/vi/E7Xu-pDp840/default.jpg )](https://www.youtube.com/watch?v=E7Xu-pDp840)


## Installation Requirements

- Python 3
- [PySide6](https://pypi.org/project/PySide6/) (a module/library in Python)
- [pyperclip](https://pypi.org/project/pyperclip/) (a module/library in Python)

## Operating System compatibility
| OS      | Compatible | Notes                                 |
|---------|------------|---------------------------------------|
| Windows | ✅          | Should work with all Windows versions |
| MacOS   | ✅          | Should work with all Mac versions     |
| Linus   | 🟨         | *Requires additional installations    |

*On Linux, `pyperclip` also requires a system clipboard tool such as `xclip`, `xsel`, or `wl-clipboard` to be installed.

```bash
pip install PySide6 pyperclip
```

## Usage

Run the application from the project root:

```bash
python main.py
```

- Use the left-hand panel to switch between your Prompt Collections and the Clipboard History.
- For an individual prompt:
  - Click **➕ Add Prompt** to add a new prompt to the current collection
  - Click **📋 Copy** to copy a prompt's text
  - Click the checkbox **(☐ or ☑)** to lock or unlock **(🔒/🔑)** the prompt for editing 
  - Click **❌ Delete** to remove the prompt.
- Click **➕ Add New Prompt Collection** to create a new collection, or use the rename/delete options to manage existing ones.
- Anything you copy elsewhere on your system while the app is running will automatically appear in the **📋 Clipboard History** panel.

## Data Storage

Prompt Collections are stored in `memory.txt` in the project root, with one collection per line in the format:

```
Collection Title, prompt one, prompt two, prompt three
```

This file is read on startup and rewritten automatically when the app closes.

## How this was Built

|   | Resource                                               |                                                                                                    | Purpose                                                                  |
|---|--------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| 1 | [Python](https://www.python.org/)                      | <img src="https://avatars.githubusercontent.com/u/1525981?s=200&v=4" height=150 alt="Python Logo"> | Programming language used                                                |
| 2 | [pyperclip](https://pypi.org/project/pyperclip/)       |                                                                                                    | Allows access to clipboard and "copy" and "paste" mechanisms             |
| 3 | [PySide6](https://doc.qt.io/qtforpython-6/index.html)  | <img src="https://doc.qt.io/qtforpython-6/_static/qtforpython.png" height=150 alt="PySide6 logo">  | A popular module/library used to make the graphical user interface (GUI) |
