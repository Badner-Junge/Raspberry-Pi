"""FamiliyOrganizer Tabs.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from config import *
import config, datetime, tkcalendar, tkinter.messagebox
import tkinter as tk


class Register:
    """Manage Tabs."""

    def cards(self):
        """Create Tabs."""
        tabControl = ttk.Notebook(self)

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht    ")
        Addings.Uebersicht(self)
        # print(tabControl.index(tabControl.select()))

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Kinder         ")
        Addings.Kinder(self)
        # print(tabControl.tab(tabControl.select(), "text"))

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Kalender     ")
        Addings.Kalender(self)

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Einkaufen   ")
        Addings.Einkaufen(self)

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Rezepte      ")
        Addings.Rezepte(self)

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Essensplan ")
        Addings.Essensplan(self)

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl


class Addings:
    """Add to Tabs."""

    def Uebersicht(self):
        """Tab1."""
        Label(
            self.tab1,
            text="Please Select your choice",
            font="Times 24 bold",
            bg="white",
            fg="blue",
            bd=10,
            relief="sunken",
        ).grid(column=1, row=2)
        Label(
            self.tab1, text="Please Select your choice", font="Times 24 bold", fg="blue"
        ).grid(column=2, row=4)
        Label(
            self.tab1,
            text="Please Select your choice",
            font="Times 24 bold",
            bg="red",
            fg="blue",
        ).grid(column=1, row=5)

    def Kinder(self):
        """Tab2."""
        Label(self.tab2, text="Hallo", width=80, height=32, bd=5, relief="sunken").grid(
            column=1, row=1
        )

    def Kalender(self):
        """Tab3."""

        Label(
            self.tab3, text="Termine", width=50, height=32, bd=5, relief="sunken"
        ).grid(column=0, row=0)

        events = {
            "2020-05-28": ("London", "meeting"),
            "2020-05-15": ("Paris", "meeting"),
            "2020-05-30": ("New York", "meeting"),
        }
        cal = Calendar(self.tab3, selectmode="day")

        for k in events.keys():
            date = datetime.datetime.strptime(k, "%Y-%m-%d").date()
            cal.calevent_create(date, events[k][0], events[k][1])

        cal.tag_config(
            "meeting", background=config.calendar[0], foreground=config.calendar[1]
        )
        cal.grid(column=1, row=0, sticky="wens")

        print("Kalender:", config.calendar)

    def Einkaufen(self):
        """Tab4."""
        Label(self.tab4, text="Please Select your choice").place(x=250, y=80)

    def Rezepte(self):
        """Tab5."""
        tree = ttk.Treeview(self.tab5, columns=("one", "two"))
        # tree["columns"] = ("one", "two")
        tree.column("one", width=config.tree[0][0])
        tree.column("two", width=config.tree[1][0])
        tree.heading("one", text=config.tree[0][1])
        tree.heading("two", text=config.tree[1][1])

        cat1 = tree.insert("", 1, "dir2", text=config.tree[-1][0])
        tree.insert(
            cat1, "end", "dir 2", text=config.tree[0][2], values=(config.tree[0][3])
        )

        cat2 = tree.insert("", 2, "dir3", text=config.tree[-1][1])
        tree.insert(
            cat2, "end", "dir 3", text=config.tree[1][2], values=(config.tree[1][3])
        )

        tree.pack(side="left", anchor="nw", fill="y")

        view = tk.Label(self.tab5, text=config.recipe[0], bg=config.recipe[1])
        view.pack(anchor="e", fill="both", expand=1)

    def Essensplan(self):
        """Tab6."""
        Label(self.tab6, text="Please Select your choice").place(x=250, y=120)
