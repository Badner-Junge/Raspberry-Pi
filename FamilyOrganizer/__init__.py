"""FamiliyOrganizer Main.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from menu import *
from modules import *
from config import *
import menu, modules, config, os, tkinter.messagebox
import tkinter as tk

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


class Root(Tk):
    """Main Window."""

    def __init__(self):
        """Initialize."""
        super(Root, self).__init__()
        self.title("Family Organizer")
        self.attributes("-fullscreen", TRUE)
        self.minsize(512, 265)
        # self.bind(
        #     "<<NotebookTabChanged>>",
        #     lambda event: event.widget.winfo_children()[
        #         event.widget.index("current")
        #     ].update(),
        # )

        menu.menuBar.createMenu(self)
        modules.Tabs.cards(self)
        config.style()

    def fullscreen_toggle(self):
        """Fullscreen from menu.py."""
        modules.fullscreen_toggle(self)

    def end(self):
        """Close Main Window."""
        root.destroy()


root = Root()
root.mainloop()
