"""FamiliyOrganizer Main.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from test_menu import *
from test_modules import *
from test_config import *
import test_menu, test_modules, test_config, os, tkinter.messagebox
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
        # self.configure(background="white")

        test_menu.menuBar.createMenu(self)
        test_modules.Tabs.cards(self)
        test_config.style()

    def fullscreen_toggle(self):
        """Fullscreen from menu.py."""
        test_modules.fullscreen_toggle(self)

    def end(self):
        """Close Main Window."""
        root.destroy()


root = Root()
root.mainloop()
