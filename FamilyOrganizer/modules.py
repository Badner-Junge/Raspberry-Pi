"""FamiliyOrganizer Modules.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from config import *
import config, datetime, tkcalendar, tkinter.messagebox, time, sys, threading
import tkinter as tk
import RPi.GPIO as GPIO

# Tabs und Inhalt erzeugen und verwalten
class Tabs:
    """Manage Tabs."""

    def cards(self):
        """Create Tabs."""
        tabControl = ttk.Notebook(self, style="main.TNotebook")

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht")
        Tabs.overview(self)
        # print(tabControl.index(tabControl.select()))

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="To-Do")
        Tabs.to_do(self)

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Kinder")
        Tabs.kids(self)
        # print(tabControl.tab(tabControl.select(), "text"))

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Kalender")
        Tabs.calendar(self)

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Einkaufen")
        Tabs.shopping(self)

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Rezepte")
        Tabs.recipes(self)

        self.tab7 = ttk.Frame(tabControl)
        tabControl.add(self.tab7, text="Essensplan")
        Tabs.meals(self)

        self.tab8 = ttk.Frame(tabControl)
        tabControl.add(self.tab8, text="Hahabu")
        Tabs.household(self)

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl

    def overview(self):
        """Tab1 Overview Sidebar."""
        tab = 1
        width = config.sidebar_buttons[8][0]

        view_frame_buttons = tk.Frame(self.tab1)
        view_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                view_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        view_frame_progress = tk.Frame(self.tab1)
        view_frame_progress.pack(side="right", anchor="e", fill="y")

        prog_1 = ttk.Progressbar(
            view_frame_progress, orient="vertical", length=500, mode="determinate",
        )
        prog_1.pack(side="right")
        prog_1["maximum"] = 100
        prog_1["value"] = 50

        prog_2 = ttk.Progressbar(
            view_frame_progress, orient="vertical", length=500, mode="determinate",
        )
        prog_2.pack(side="right", fill="y")
        prog_2["maximum"] = 100
        prog_2["value"] = 20

    def to_do(self):
        """Tab2 To-Do Sidebar."""
        tab = 2

        todo_frame_buttons = tk.Frame(self.tab2)
        todo_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                todo_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

    def kids(self):
        """Tab2 Kids Sidebar."""
        tab = 3

        kids_frame_buttons = tk.Frame(self.tab3)
        kids_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                kids_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        """Tab3 Register."""
        kids_frame = tk.Frame(self.tab3)
        kids_frame.pack(side="right", anchor="n", fill="both", expand=1)

        tabkids = ttk.Notebook(kids_frame, style="kids.TNotebook")

        self.tabkids1 = ttk.Frame(tabkids)
        tabkids.add(self.tabkids1, text="Fabienne")

        self.tabkids2 = ttk.Frame(tabkids)
        tabkids.add(self.tabkids2, text="Mio")

        self.tabkids3 = ttk.Frame(tabkids)
        tabkids.add(self.tabkids3, text="Mika")

        self.tabkids4 = ttk.Frame(tabkids)
        tabkids.add(self.tabkids4, text="Jona")

        tabkids.pack(expand=1, fill="both")

        self.tab_kids = tabkids

    def calendar(self):
        """Tab3 Calendar Sidebar."""
        tab = 4

        cal_frame_buttons = tk.Frame(self.tab4)
        cal_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                cal_frame_buttons,
                text=txt,
                bg=col,
                padx=0,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        """Tab4 Calendar."""
        events = {
            "2020-06-28": ("London", "meeting"),
            "2020-06-15": ("Paris", "meeting"),
            "2020-06-30": ("New York", "meeting"),
        }
        cal = Calendar(self.tab4, selectmode="day")

        for k in events.keys():
            date = datetime.datetime.strptime(k, "%Y-%m-%d").date()
            cal.calevent_create(date, events[k][0], events[k][1])

        cal.tag_config(
            "meeting", background=config.calendar[0], foreground=config.calendar[1]
        )
        cal.pack(side="right", fill="both", expand=1)

    def shopping(self):
        """Tab5 Shopping Sidebar."""
        tab = 5

        shop_frame_buttons = tk.Frame(self.tab5)
        shop_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                shop_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        """Tab5 Listbox."""
        Listbox(self.tab5).pack(side="right", fill="both", expand=True)

        """Tab5 Treeview."""
        shop_tree = ttk.Treeview(self.tab5)

        cat1 = shop_tree.insert("", 1, "dir2", text=config.shop[-1][0])
        shop_tree.insert(
            cat1, "end", "dir 2", text=config.shop[0][2], values=(config.shop[0][3])
        )

        cat2 = shop_tree.insert("", 2, "dir3", text=config.shop[-1][1])
        shop_tree.insert(
            cat2, "end", "dir 3", text=config.shop[1][2], values=(config.shop[1][3])
        )

        cat3 = shop_tree.insert("", 3, "dir4", text=config.shop[-1][2])
        shop_tree.insert(
            cat3, "end", "dir 4", text=config.shop[2][2], values=(config.shop[2][3])
        )

        shop_tree.pack(side="right", anchor="nw", fill="both", expand=True)

    def recipes(self):
        """Tab5 Recipes Sidebar."""
        tab = 6

        rec_frame_buttons = tk.Frame(self.tab6)
        rec_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                rec_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        """Tab6 Treeview."""
        tree = ttk.Treeview(self.tab6, columns=(config.recipe[0]))
        # tree["columns"] = ("one", "two")
        recipe = 0
        column = 0
        while column < len(config.recipe[0]):
            tree.column(config.recipe[0][column], width=config.recipe[2][0])
            tree.heading(config.recipe[0][column], text=config.recipe[1][column])
            column += 1
        while recipe < len(config.recipe[-1]):
            cat = tree.insert(
                "",
                config.recipe[3][recipe],
                config.recipe[4][recipe],
                text=config.recipe[-1][recipe],
            )
            cat_sub1 = tree.insert(
                cat,
                "end",
                config.recipe[5][recipe],
                text=config.recipe[7][recipe],
                values=10,
            )
            cat_sub2 = tree.insert(
                cat_sub1, "end", config.recipe[6][recipe], text=config.recipe[8],
            )
            recipe += 1

        tree.pack(side="right", anchor="nw", fill="both", expand=True)

    def meals(self):
        """Tab6 Meal Sidebar."""
        tab = 7

        meal_frame_buttons = tk.Frame(self.tab7)
        meal_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                meal_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        """Tab7 Days."""
        v = IntVar()
        v.set(0)

        day_frame = tk.Frame(self.tab7)
        day_frame.pack(side="left", fill="both", expand=True)
        Label1 = Label(
            day_frame, text="Wochentag", bd=5, relief="sunken", font="Times 24 bold"
        ).pack()

        for txt in config.meal[0][1]:
            Label(day_frame, text=txt, font="Times 24").pack(fill="y", expand=True)

        """Tab6 Frame this week."""
        this_week_frame = tk.Frame(self.tab7)
        this_week_frame.pack(side="left", fill="y", expand=True)
        Label2 = Label(
            this_week_frame,
            text="aktuelle Woche",
            bd=5,
            relief="sunken",
            font="Times 24 bold",
        ).pack()

        for txt, val in config.meal[1][0]:
            Radiobutton(
                this_week_frame,
                text=txt,
                indicatoron=0,
                width=16,
                padx=10,
                variable=v,
                value=val,
                font="Times 18",
            ).pack(fill="y", expand=True)

        """Tab6 Frame next week."""
        next_week_frame = tk.Frame(self.tab7)
        next_week_frame.pack(side="left", fill="y", expand=True)
        Label3 = Label(
            next_week_frame,
            text="nächste Woche",
            bd=5,
            relief="sunken",
            font="Times 24 bold",
        ).pack()

        for txt, val in config.meal[1][1]:
            Radiobutton(
                next_week_frame,
                text=txt,
                indicatoron=0,
                width=16,
                padx=10,
                variable=v,
                value=val,
                font="Times 18",
            ).pack(fill="y", expand=True)

    def household(self):
        """Tab8 Household Sidebar."""
        tab = 8

        home_frame_buttons = tk.Frame(self.tab8)
        home_frame_buttons.pack(side="right", anchor="e", fill="y")

        for txt, col, val in config.sidebar_buttons[tab]:
            Button(
                home_frame_buttons,
                text=txt,
                bg=col,
                width=config.sidebar_buttons[0][0],
                font=config.sidebar_buttons[0][1],
                command=val,
            ).pack(fill="y", expand=1)

        budget_frame = tk.Frame(self.tab8, bd=5, relief="sunken")
        budget_frame.pack(side="top", fill="y")

        budget_in_label = tk.Label(budget_frame, text="Einnahmen: ").grid(
            column=1, row=1
        )
        budget_in_last = tk.Label(budget_frame, text="20,00€ (letzte: 10,00€)").grid(
            column=2, row=1
        )

        budget_out_label = tk.Label(budget_frame, text="Ausgaben: ").grid(
            column=1, row=2
        )
        budget_out_last = tk.Label(budget_frame, text="10,00€ (letzte: 5,00€)").grid(
            column=2, row=2
        )

        wood_frame = tk.Frame(self.tab8, bd=5, relief="sunken")
        wood_frame.pack(side="left", fill="y")

        wood_counter = tk.Label(wood_frame, text="Holz").grid(column=1, row=1)
        wood_label = tk.Label(wood_frame, text="noch da").grid(column=2, row=2)


def top_window(args):
    """Create Toplevel Windows."""
    # Overview
    if args >= 1 and args < 7:
        if args == 1:
            """Overview 1."""
            meal_add = Toplevel()
            meal_add.title(config.sidebar_buttons[1][0][0])
            meal_add.geometry("+%d+%d" % (400, 200))
            meal_add_label1 = tk.Label(meal_add, text="Rezept:").grid(column=1, row=1)
            meal_add_label2 = tk.Label(meal_add, text="Zutaten:").grid(column=1, row=2)
            meal_add_label3 = tk.Label(meal_add, text="Anleitung:").grid(
                column=1, row=3
            )

            meal_add_entry1 = tk.Entry(meal_add).grid(column=2, row=1)
            meal_add_entry2 = tk.Entry(meal_add).grid(column=2, row=2)
            meal_add_entry3 = tk.Entry(meal_add).grid(column=2, row=3)

            meal_add_button1 = tk.Button(meal_add, text="OK").grid(column=1, row=4)
            meal_add_button2 = tk.Button(
                meal_add, text="Abbrechen", command=meal_add.destroy
            ).grid(column=2, row=4)
        elif args == 2:
            """Essen ändern."""
            meal_edit = Toplevel()
            meal_edit.title(config.sidebar_buttons[1][1][0])
            meal_edit.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                meal_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0]:
                Radiobutton(
                    meal_edit,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=meal_edit.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 3:
            """?."""
            meal_del = Toplevel()
            meal_del.title(config.sidebar_buttons[1][2][0])
            meal_del.geometry("+%d+%d" % (400, 200))
            meal_del_label = tk.Label(meal_del, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            meal_del_entry = tk.Entry(meal_del).grid(column=2, row=1)
            meal_del_button1 = tk.Button(meal_del, text="OK").grid(column=1, row=2)
            meal_del_button2 = tk.Button(
                meal_del, text="Abbrechen", command=meal_del.destroy
            ).grid(column=2, row=2)
        elif args == 4:
            """Einzelnen Tag löschen."""
            day_del = tk.messagebox.askquestion(
                config.sidebar_buttons[1][3][0],
                "Möchtest du einen Tag wirklich löschen?",
                icon="warning",
            )
            if day_del == "yes":
                print("Ein Tag gelöscht")
            else:
                print("Ein Tag nicht gelöscht")
        elif args == 5:
            """Woche 1 löschen."""
            week1_del = tk.messagebox.askquestion(
                config.sidebar_buttons[1][4][0],
                "Möchtest du Woche 1 wirklich löschen?",
                icon="warning",
            )
            if week1_del == "yes":
                print("Woche 1 gelöscht")
            else:
                print("Woche 1 nicht gelöscht")
        elif args == 6:
            """Woche 2 löschen."""
            week2_del = tk.messagebox.askquestion(
                config.sidebar_buttons[1][5][0],
                "Möchtest du Woche 2 wirklich löschen?",
                icon="warning",
            )
            if week2_del == "yes":
                print("Woche 2 gelöscht")
            else:
                print("Woche 2 nicht gelöscht")
    # To-Do
    elif args >= 7 and args < 13:
        if args == 7:
            """Essen hinzufügen."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][0][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
        elif args == 8:
            """Essen ändern."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][1][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
        elif args == 9:
            """?."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][2][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
        elif args == 10:
            """Einzelnen Tag löschen."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][3][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
        elif args == 11:
            """Woche 1 löschen."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][4][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
        elif args == 12:
            """Woche 2 löschen."""
            todo_add = Toplevel()
            todo_add.title(config.sidebar_buttons[2][5][0])
            todo_add.geometry("+%d+%d" % (400, 200))
            todo_add_label1 = tk.Label(todo_add, text="To-Do:").grid(column=1, row=1)
            todo_add_label2 = tk.Label(todo_add, text="Datum:").grid(column=1, row=2)
            todo_add_label3 = tk.Label(todo_add, text="Uhrzeit:").grid(column=1, row=3)

            todo_add_entry1 = tk.Entry(todo_add).grid(column=2, row=1)
            todo_add_entry2 = tk.Entry(todo_add).grid(column=2, row=2)
            todo_add_entry3 = tk.Entry(todo_add).grid(column=2, row=3)

            todo_add_button1 = tk.Button(todo_add, text="OK").grid(column=1, row=4)
            todo_add_button2 = tk.Button(
                todo_add, text="Abbrechen", command=todo_add.destroy
            ).grid(column=2, row=4)
    # Kids
    elif args >= 13 and args < 19:
        if args == 13:
            """Essen hinzufügen."""
            kids_add = Toplevel()
            kids_add.title(config.sidebar_buttons[3][0][0])
            kids_add.geometry("+%d+%d" % (400, 200))
            kids_add_label1 = tk.Label(kids_add, text="Rezept:").grid(column=1, row=1)
            kids_add_label2 = tk.Label(kids_add, text="Zutaten:").grid(column=1, row=2)
            kids_add_label3 = tk.Label(kids_add, text="Anleitung:").grid(
                column=1, row=3
            )

            kids_add_entry1 = tk.Entry(kids_add).grid(column=2, row=1)
            kids_add_entry2 = tk.Entry(kids_add).grid(column=2, row=2)
            kids_add_entry3 = tk.Entry(kids_add).grid(column=2, row=3)

            kids_add_button1 = tk.Button(kids_add, text="OK").grid(column=1, row=4)
            kids_add_button2 = tk.Button(
                kids_add, text="Abbrechen", command=kids_add.destroy
            ).grid(column=2, row=4)
        elif args == 14:
            """Essen ändern."""
            kids_edit = Toplevel()
            kids_edit.title(config.sidebar_buttons[3][1][0])
            kids_edit.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                kids_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0]:
                Radiobutton(
                    kids_edit,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=kids_edit.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 15:
            """?."""
            kids_del = Toplevel()
            kids_del.title(config.sidebar_buttons[3][2][0])
            kids_del.geometry("+%d+%d" % (400, 200))
            kids_del_label = tk.Label(kids_del, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            kids_del_entry = tk.Entry(kids_del).grid(column=2, row=1)
            kids_del_button1 = tk.Button(kids_del, text="OK").grid(column=1, row=2)
            kids_del_button2 = tk.Button(
                kids_del, text="Abbrechen", command=kids_del.destroy
            ).grid(column=2, row=2)
        elif args == 16:
            """Einzelnen Tag löschen."""
            kids_del = tk.messagebox.askquestion(
                config.sidebar_buttons[3][3][0],
                "Möchtest du einen Tag wirklich löschen?",
                icon="warning",
            )
            if kids_del == "yes":
                print("Ein Tag gelöscht")
            else:
                print("Ein Tag nicht gelöscht")
        elif args == 17:
            """Woche 1 löschen."""
            kids_del = tk.messagebox.askquestion(
                config.sidebar_buttons[3][4][0],
                "Möchtest du Woche 1 wirklich löschen?",
                icon="warning",
            )
            if kids_del == "yes":
                print("Woche 1 gelöscht")
            else:
                print("Woche 1 nicht gelöscht")
        elif args == 18:
            """Woche 2 löschen."""
            kids_del = tk.messagebox.askquestion(
                config.sidebar_buttons[3][5][0],
                "Möchtest du Woche 2 wirklich löschen?",
                icon="warning",
            )
            if kids_del == "yes":
                print("Woche 2 gelöscht")
            else:
                print("Woche 2 nicht gelöscht")
    # Calendar
    elif args >= 19 and args < 25:
        if args == 19:
            """zu Essensplan."""
            cal_view = Toplevel()
            cal_view.title(config.sidebar_buttons[4][0][0])
            cal_view.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                cal_view, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0][0]:
                Radiobutton(
                    cal_view,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=cal_view.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 20:
            """neue Kategorie."""
            categorie_new = Toplevel()
            categorie_new.title(config.sidebar_buttons[4][1][0])
            categorie_new.geometry("+%d+%d" % (400, 200))
            cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
            cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
            cat_new_button2 = tk.Button(
                categorie_new, text="Abbrechen", command=categorie_new.destroy
            ).grid(column=2, row=2)
        elif args == 21:
            """neues Rezept."""
            recipe_new = Toplevel()
            recipe_new.title(config.sidebar_buttons[4][2][0])
            recipe_new.geometry("+%d+%d" % (400, 200))
            rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
                column=1, row=1
            )
            rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
            rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

            rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
            rec_new_button2 = tk.Button(
                recipe_new, text="Abbrechen", command=recipe_new.destroy
            ).grid(column=2, row=4)
        elif args == 22:
            """Rezept ändern."""
            recipe_edit = Toplevel()
            recipe_edit.title(config.sidebar_buttons[4][3][0])
            recipe_edit.geometry("+%d+%d" % (400, 200))
            rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(
                column=1, row=1
            )
            rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
            rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
            rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

            rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
            rec_edit_button2 = tk.Button(
                recipe_edit, text="Abbrechen", command=recipe_edit.destroy
            ).grid(column=2, row=4)
        elif args == 23:
            """Rezept ändern."""
            recipe_edit = Toplevel()
            recipe_edit.title(config.sidebar_buttons[4][4][0])
            recipe_edit.geometry("+%d+%d" % (400, 200))
            rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(
                column=1, row=1
            )
            rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
            rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
            rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

            rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
            rec_edit_button2 = tk.Button(
                recipe_edit, text="Abbrechen", command=recipe_edit.destroy
            ).grid(column=2, row=4)
        elif args == 24:
            """Rezept löschen."""
            recipe_del = tk.messagebox.askquestion(
                config.sidebar_buttons[4][5][0],
                "Möchtest du den Termin wirklich löschen?",
                icon="warning",
            )
            if recipe_del == "yes":
                print("Termin gelöscht")
            else:
                print("Termin nicht gelöscht")
    # Shopping
    elif args >= 25 and args < 31:
        if args == 25:
            """Rezept anzeigen."""
            recipe_view = Toplevel()
            recipe_view.title(config.sidebar_buttons[5][0][0])
            recipe_view.geometry("+%d+%d" % (400, 200))
            rec_view_label1 = tk.Label(recipe_view, text="Rezept:").grid(
                column=1, row=1
            )
            rec_view_label2 = tk.Label(recipe_view, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_view_label3 = tk.Label(recipe_view, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_view_entry1 = tk.Entry(recipe_view).grid(column=2, row=1)
            rec_view_entry2 = tk.Entry(recipe_view).grid(column=2, row=2)
            rec_view_entry3 = tk.Entry(recipe_view).grid(column=2, row=3)

            rec_view_button1 = tk.Button(recipe_view, text="OK").grid(column=1, row=4)
            rec_view_button2 = tk.Button(
                recipe_view, text="Abbrechen", command=recipe_view.destroy
            ).grid(column=2, row=4)
        elif args == 26:
            """zu Essensplan."""
            recipe_add = Toplevel()
            recipe_add.title(config.sidebar_buttons[5][1][0])
            recipe_add.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                recipe_add, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0]:
                Radiobutton(
                    recipe_add,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=recipe_add.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 27:
            """neue Kategorie."""
            categorie_new = Toplevel()
            categorie_new.title(config.sidebar_buttons[5][2][0])
            categorie_new.geometry("+%d+%d" % (400, 200))
            cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
            cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
            cat_new_button2 = tk.Button(
                categorie_new, text="Abbrechen", command=categorie_new.destroy
            ).grid(column=2, row=2)
        elif args == 28:
            """neues Rezept."""
            recipe_new = Toplevel()
            recipe_new.title(config.sidebar_buttons[5][3][0])
            recipe_new.geometry("+%d+%d" % (400, 200))
            rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
                column=1, row=1
            )
            rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
            rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

            rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
            rec_new_button2 = tk.Button(
                recipe_new, text="Abbrechen", command=recipe_new.destroy
            ).grid(column=2, row=4)
        elif args == 29:
            """Rezept ändern."""
            recipe_edit = Toplevel()
            recipe_edit.title(config.sidebar_buttons[5][4][0])
            recipe_edit.geometry("+%d+%d" % (400, 200))
            rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(
                column=1, row=1
            )
            rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
            rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
            rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

            rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
            rec_edit_button2 = tk.Button(
                recipe_edit, text="Abbrechen", command=recipe_edit.destroy
            ).grid(column=2, row=4)
        elif args == 30:
            """Rezept löschen."""
            recipe_del = tk.messagebox.askquestion(
                config.sidebar_buttons[5][5][0],
                "Möchtest du das Rezept wirklich löschen?",
                icon="warning",
            )
            if recipe_del == "yes":
                print("Rezept gelöscht")
            else:
                print("Rezept nicht gelöscht")
    # Recipes
    elif args >= 31 and args < 37:
        if args == 31:
            """Rezept anzeigen."""
            recipe_view = Toplevel()
            recipe_view.title(config.sidebar_buttons[6][0][0])
            recipe_view.geometry("+%d+%d" % (400, 200))
            rec_view_label1 = tk.Label(recipe_view, text="Rezept:").grid(
                column=1, row=1
            )
            rec_view_label2 = tk.Label(recipe_view, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_view_label3 = tk.Label(recipe_view, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_view_entry1 = tk.Entry(recipe_view).grid(column=2, row=1)
            rec_view_entry2 = tk.Entry(recipe_view).grid(column=2, row=2)
            rec_view_entry3 = tk.Entry(recipe_view).grid(column=2, row=3)

            rec_view_button1 = tk.Button(recipe_view, text="OK").grid(column=1, row=4)
            rec_view_button2 = tk.Button(
                recipe_view, text="Abbrechen", command=recipe_view.destroy
            ).grid(column=2, row=4)
        elif args == 32:
            """zu Essensplan."""
            recipe_add = Toplevel()
            recipe_add.title(config.sidebar_buttons[6][1][0])
            recipe_add.geometry("+%d+%d" % (400, 200))

            recipe_thisweek = Radiobutton(
                recipe_add, text="Aktuelle Woche", indicatoron=0
            ).grid(column=1, row=1)
            recipe_nextweek = Radiobutton(
                recipe_add, text="Nächste Woche", indicatoron=0, value=0
            ).grid(column=2, row=1)

            v = IntVar()
            v.set(1)

            for txt, val in config.meal[0][0]:
                Radiobutton(
                    recipe_add,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=recipe_add.destroy,
                    value=val,
                ).grid(column=1, columnspan=2)
        elif args == 33:
            """neue Kategorie."""
            categorie_new = Toplevel()
            categorie_new.title(config.sidebar_buttons[6][2][0])
            categorie_new.geometry("+%d+%d" % (400, 200))
            cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
            cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
            cat_new_button2 = tk.Button(
                categorie_new, text="Abbrechen", command=categorie_new.destroy
            ).grid(column=2, row=2)
        elif args == 34:
            """neues Rezept."""
            recipe_new = Toplevel()
            recipe_new.title(config.sidebar_buttons[6][3][0])
            recipe_new.geometry("+%d+%d" % (400, 200))
            rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
                column=1, row=1
            )
            rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
            rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
            rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

            rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
            rec_new_button2 = tk.Button(
                recipe_new, text="Abbrechen", command=recipe_new.destroy
            ).grid(column=2, row=4)
        elif args == 35:
            """Rezept ändern."""
            recipe_edit = Toplevel()
            recipe_edit.title(config.sidebar_buttons[6][4][0])
            recipe_edit.geometry("+%d+%d" % (400, 200))
            rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(
                column=1, row=1
            )
            rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(
                column=1, row=2
            )
            rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(
                column=1, row=3
            )

            rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
            rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
            rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

            rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
            rec_edit_button2 = tk.Button(
                recipe_edit, text="Abbrechen", command=recipe_edit.destroy
            ).grid(column=2, row=4)
        elif args == 36:
            """Rezept löschen."""
            recipe_del = tk.messagebox.askquestion(
                config.sidebar_buttons[6][5][0],
                "Möchtest du das Rezept wirklich löschen?",
                icon="warning",
            )
            if recipe_del == "yes":
                print("Rezept gelöscht")
            else:
                print("Rezept nicht gelöscht")
    # Meal
    elif args >= 37 and args < 43:
        if args == 37:
            """Essen hinzufügen."""
            meal_add = Toplevel()
            meal_add.title(config.sidebar_buttons[7][0][0])
            meal_add.geometry("+%d+%d" % (400, 200))
            meal_add_label1 = tk.Label(meal_add, text="Rezept:").grid(column=1, row=1)
            meal_add_label2 = tk.Label(meal_add, text="Zutaten:").grid(column=1, row=2)
            meal_add_label3 = tk.Label(meal_add, text="Anleitung:").grid(
                column=1, row=3
            )

            meal_add_entry1 = tk.Entry(meal_add).grid(column=2, row=1)
            meal_add_entry2 = tk.Entry(meal_add).grid(column=2, row=2)
            meal_add_entry3 = tk.Entry(meal_add).grid(column=2, row=3)

            meal_add_button1 = tk.Button(meal_add, text="OK").grid(column=1, row=4)
            meal_add_button2 = tk.Button(
                meal_add, text="Abbrechen", command=meal_add.destroy
            ).grid(column=2, row=4)
        elif args == 38:
            """Essen ändern."""
            meal_edit = Toplevel()
            meal_edit.title(config.sidebar_buttons[7][1][0])
            meal_edit.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                meal_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0]:
                Radiobutton(
                    meal_edit,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=meal_edit.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 39:
            """?."""
            meal_del = Toplevel()
            meal_del.title(config.sidebar_buttons[7][2][0])
            meal_del.geometry("+%d+%d" % (400, 200))
            meal_del_label = tk.Label(meal_del, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            meal_del_entry = tk.Entry(meal_del).grid(column=2, row=1)
            meal_del_button1 = tk.Button(meal_del, text="OK").grid(column=1, row=2)
            meal_del_button2 = tk.Button(
                meal_del, text="Abbrechen", command=meal_del.destroy
            ).grid(column=2, row=2)
        elif args == 40:
            """Einzelnen Tag löschen."""
            day_del = tk.messagebox.askquestion(
                config.sidebar_buttons[7][3][0],
                "Möchtest du einen Tag wirklich löschen?",
                icon="warning",
            )
            if day_del == "yes":
                print("Ein Tag gelöscht")
            else:
                print("Ein Tag nicht gelöscht")
        elif args == 41:
            """Woche 1 löschen."""
            week1_del = tk.messagebox.askquestion(
                config.sidebar_buttons[7][4][0],
                "Möchtest du Woche 1 wirklich löschen?",
                icon="warning",
            )
            if week1_del == "yes":
                print("Woche 1 gelöscht")
            else:
                print("Woche 1 nicht gelöscht")
        elif args == 42:
            """Woche 2 löschen."""
            week2_del = tk.messagebox.askquestion(
                config.sidebar_buttons[7][5][0],
                "Möchtest du Woche 2 wirklich löschen?",
                icon="warning",
            )
            if week2_del == "yes":
                print("Woche 2 gelöscht")
            else:
                print("Woche 2 nicht gelöscht")
    # Household
    elif args >= 43 and args < 49:
        if args == 43:
            """Essen hinzufügen."""
            meal_add = Toplevel()
            meal_add.title(config.sidebar_buttons[8][0][0])
            meal_add.geometry("+%d+%d" % (400, 200))
            meal_add_label1 = tk.Label(meal_add, text="Rezept:").grid(column=1, row=1)
            meal_add_label2 = tk.Label(meal_add, text="Zutaten:").grid(column=1, row=2)
            meal_add_label3 = tk.Label(meal_add, text="Anleitung:").grid(
                column=1, row=3
            )

            meal_add_entry1 = tk.Entry(meal_add).grid(column=2, row=1)
            meal_add_entry2 = tk.Entry(meal_add).grid(column=2, row=2)
            meal_add_entry3 = tk.Entry(meal_add).grid(column=2, row=3)

            meal_add_button1 = tk.Button(meal_add, text="OK").grid(column=1, row=4)
            meal_add_button2 = tk.Button(
                meal_add, text="Abbrechen", command=meal_add.destroy
            ).grid(column=2, row=4)
        elif args == 44:
            """Essen ändern."""
            meal_edit = Toplevel()
            meal_edit.title(config.sidebar_buttons[8][1][0])
            meal_edit.geometry("+%d+%d" % (400, 200))

            v = IntVar()
            v.set(1)

            Label(
                meal_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,
            ).pack()

            for txt, val in config.meal[0]:
                Radiobutton(
                    meal_edit,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=v,
                    command=meal_edit.destroy,
                    value=val,
                ).pack(anchor=W)
        elif args == 45:
            """?."""
            meal_del = Toplevel()
            meal_del.title(config.sidebar_buttons[8][2][0])
            meal_del.geometry("+%d+%d" % (400, 200))
            meal_del_label = tk.Label(meal_del, text="Neue Kategorie:").grid(
                column=1, row=1
            )
            meal_del_entry = tk.Entry(meal_del).grid(column=2, row=1)
            meal_del_button1 = tk.Button(meal_del, text="OK").grid(column=1, row=2)
            meal_del_button2 = tk.Button(
                meal_del, text="Abbrechen", command=meal_del.destroy
            ).grid(column=2, row=2)
        elif args == 46:
            """Einzelnen Tag löschen."""
            day_del = tk.messagebox.askquestion(
                config.sidebar_buttons[8][3][0],
                "Möchtest du einen Tag wirklich löschen?",
                icon="warning",
            )
            if day_del == "yes":
                print("Ein Tag gelöscht")
            else:
                print("Ein Tag nicht gelöscht")
        elif args == 47:
            """Woche 1 löschen."""
            week1_del = tk.messagebox.askquestion(
                config.sidebar_buttons[8][4][0],
                "Möchtest du Woche 1 wirklich löschen?",
                icon="warning",
            )
            if week1_del == "yes":
                print("Woche 1 gelöscht")
            else:
                print("Woche 1 nicht gelöscht")
        elif args == 48:
            """Woche 2 löschen."""
            week2_del = tk.messagebox.askquestion(
                config.sidebar_buttons[8][5][0],
                "Möchtest du Woche 2 wirklich löschen?",
                icon="warning",
            )
            if week2_del == "yes":
                print("Woche 2 gelöscht")
            else:
                print("Woche 2 nicht gelöscht")


def top_config(self):
    """?."""
    config_window = Toplevel()
    config_window.title("Konfiguration")
    config_window.geometry("+%d+%d" % (400, 200))

    config_window_button1 = tk.Button(config_window, text="OK").grid(column=1, row=1)
    config_window_button2 = tk.Button(
        config_window, text="Abbrechen", command=config_window.destroy
    ).grid(column=2, row=1)


def fullscreen_toggle(self):
    """Switch Fullscreen on/off."""
    if self.attributes("-fullscreen") == FALSE:
        self.attributes("-fullscreen", TRUE)
    else:
        self.attributes("-fullscreen", FALSE)
