#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import os

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Family Organizer")
        self.attributes("-fullscreen", False)
        self.minsize(512, 265)
        self.maxsize(1024, 530)
        self.configure(background="white")

        self.createMenu()

        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Kinder")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Kalender")

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Einkaufen")

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Rezepte")

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Essensplan")

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl

    def end(self):
        root.destroy()

    def createMenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Beenden", command=self.end)

        visual_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Darstellung", menu=visual_menu)
        visual_menu.add_command(
            label="Vollbild", command=self.attributes("-fullscreen", False)
        )

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us")


root = Root()
root.mainloop()
