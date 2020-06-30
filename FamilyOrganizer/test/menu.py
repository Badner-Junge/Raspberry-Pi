"""FamiliyOrganizer Menü.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from config import *
from modules import *
import modules, config, tkinter.messagebox
import tkinter as tk


class menuBar:
    """Create Menubar."""

    def createMenu(self):
        """Create Menu Categories."""
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Beenden", command=self.end)

        option_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Optionen", menu=option_menu)
        option_menu.add_command(label="Vollbild", command=self.fullscreen_toggle)
        option_menu.add_command(label="Lüftersteuerung")
        option_menu.add_command(label="Refresh")

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us")
