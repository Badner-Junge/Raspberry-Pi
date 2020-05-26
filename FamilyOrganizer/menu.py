# FamiliyOrganizer Menü
# Version: 0.1
# Geschrieben von Fabian Rieger

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import os

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


class menuBar:
    """Create Menubar"""

    def createMenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Beenden", command=self.end)

        visual_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Darstellung", menu=visual_menu)
        visual_menu.add_command(label="Vollbild", command=self.fullscreen_toggle)
        # visual_menu.add_command(label="Vollbild aus", command=self.fullscreen_off)

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us")

    # def fullscreen_on(self):
    #     self.attributes("-fullscreen", TRUE)

    # def fullscreen_off(self):
    #     self.attributes("-fullscreen", FALSE)

    # def end(self):
    #     root.destroy()
