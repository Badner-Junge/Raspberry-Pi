"""FamiliyOrganizer Modules.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from config import *
import config, datetime, tkcalendar, tkinter.messagebox, time, sys, threading, sqlite3
import tkinter as tk
import RPi.GPIO as GPIO

# SECTION Tabs
class Tabs:
    """Manage Tabs."""

    # ANCHOR Reiter
    def cards(self):
        """Create Tabs."""
        global tabControl
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

    # ANCHOR Übersicht
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

    # ANCHOR To-Do
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

    # ANCHOR Kinder
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

    # ANCHOR Kalender
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

    # ANCHOR Einkaufen
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

    # ANCHOR Rezepte
    def recipes(self):
        """Tab5 Recipes Sidebar."""
        tab = 6
        global tree, recipe, categorie, index, rec_cat

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

        """Tab5 Treeview."""
        tree = ttk.Treeview(self.tab6, columns=(config.recipe[1]))
        column = 0
        categorie = 0
        recipe = 0

        # Selektion Rückgabewert
        def on_tree_select(self):
            global selection_rec
            for item in tree.selection():
                selection_rec = tree.item(item, "text")
                # print(selection_rec)

        tree.bind("<<TreeviewSelect>>", on_tree_select)

        # Erzeuge Scrollbar
        scbTree = tk.Scrollbar(self.tab6, orient="vertical", command=tree.yview)
        scbTree.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scbTree.set)

        # Erzeugt Spalten
        for col in config.recipe[1]:
            tree.column(config.recipe[1][column], width=config.recipe[3][0])
            tree.heading(config.recipe[1][column], text=config.recipe[2][column])
            column += 1

        # Erzeugt Kategorien
        for cat in config.recipe[4]:
            cat = tree.insert(
                "",
                config.recipe[4][categorie],
                config.recipe[6][categorie],
                text=config.recipe[5][categorie],
            )
            # print(config.recipe[5][categorie])
            rec = config.recipe[5][categorie]
            con = sqlite3.connect("family_data.db")
            cursor = con.cursor()
            cursor.execute(
                "SELECT * FROM rec_recipe WHERE rec_categorie LIKE ?",
                ("%" + str(rec)[2:-3] + "%",),
            )
            rec_cat = cursor.fetchall()

            # Setzt vorhandene Rezepte in Kategorien ein
            index = 0
            for i in rec_cat:
                tree.insert(
                    cat,
                    "end",
                    i + config.recipe[7][index],
                    text=rec_cat[index][2],
                    values=[rec_cat[index][6], rec_cat[index][7]],
                )
                index += 1
            cursor.close()
            con.close()
            recipe += 1
            categorie += 1

        # cat_sub2 = tree.insert(
        #     cat_sub1, "end", config.recipe[8][recipe], text=config.recipe[12],
        # )

        tree.pack(side="right", anchor="nw", fill="both", expand=True)

    # ANCHOR Essensplan
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

        """Tab6 Days."""
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

    # ANCHOR Haushaltsbuch
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


# SECTION Fenster
def top_window(args):
    """Create Toplevel Windows."""
    # SECTION Overview
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
    # SECTION To-Do
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
    # SECTION Kids
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
    # SECTION Calendar
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
    # SECTION Shopping
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
    # SECTION Recipes
    elif args >= 31 and args < 37:
        # ANCHOR Rezept anzeigen
        if args == 31:
            """Rezept anzeigen."""
            # Fenster erzeugen
            recipe_view = Toplevel()
            recipe_view.title(config.sidebar_buttons[6][0][0])
            recipe_view.geometry("+%d+%d" % (250, 50))
            recipe_view["height"] = 480
            recipe_view["width"] = 600

            # Kategorie auslesen
            def categorie():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT rec_categorie FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    txCategorie.insert("end", dsatz[0])
                    print(dsatz)
                    txCategorie.config(state="disabled")
                cursor.close()
                con.close()

            # Dauer auslesen
            def time():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT time FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    txTime.insert("end", dsatz[0])
                    txTime.config(state="disabled")
                cursor.close()
                con.close()

            # Name auslesen
            def name():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT name FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    txName.insert("end", dsatz[0])
                    txName.config(state="disabled")
                cursor.close()
                con.close()

            # Zutaten auslesen
            def ingredient():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT ingredient FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    txIngredient.insert("end", dsatz[0])
                    txIngredient.config(state="disabled")
                cursor.close()
                con.close()

            # Mengen auslesen
            def measurement():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT measurement FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    txMeasurement.insert("end", dsatz[0])
                    txMeasurement.config(state="disabled")
                cursor.close()
                con.close()

            # Anleitung auslesen
            def recipe():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT recipe FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    txRecipe.insert("end", dsatz[0])
                    txRecipe.config(state="disabled")
                cursor.close()
                con.close()

            # Scrollbarverknüpfung Zutaten und Mengen
            def multi_scrollbar(*args):
                txMeasurement.yview(*args)
                txMeasurement.configure(yscrollcommand=scbMeasurement.set)
                txIngredient.yview(*args)
                txIngredient.configure(yscrollcommand=scbIngredient.set)

            # Anzeige Rezept
            lbName = tk.Label(recipe_view, text="Rezept:")
            lbName.place(x=10, y=10)
            txName = tk.Text(recipe_view, width=60, height=1)
            txName.place(x=90, y=10)

            # Anzeige Kategorie
            lbCategorie = tk.Label(recipe_view, text="Kategorie:")
            lbCategorie.place(x=10, y=40)
            txCategorie = tk.Text(recipe_view, width=15, height=1)
            txCategorie.place(x=90, y=40)

            # Anzeige Dauer
            lbTime = tk.Label(recipe_view, text="Dauer:")
            lbTime.place(x=220, y=40)
            txTime = tk.Text(recipe_view, width=15, height=1)
            txTime.place(x=270, y=40)

            # Anzeige und Scrollbar Zutaten
            lbIngredient = tk.Label(recipe_view, text="Zutaten:")
            lbIngredient.place(x=10, y=70)
            frIngredient = tk.Frame(recipe_view)
            frIngredient.place(x=90, y=70)
            scbIngredient = tk.Scrollbar(
                frIngredient, orient="vertical", command=multi_scrollbar
            )
            txIngredient = tk.Text(frIngredient, width=36, height=8)
            txIngredient.pack(side="left")
            scbIngredient.pack(side="left", fill="y")

            # Anzeige und Scrollbar Mengen
            lbMeasurement = tk.Label(recipe_view, text="Menge:")
            lbMeasurement.place(x=410, y=70)
            frMeasurement = tk.Frame(recipe_view)
            frMeasurement.place(x=475, y=70)
            scbMeasurement = tk.Scrollbar(
                frMeasurement, orient="vertical", command=multi_scrollbar
            )
            txMeasurement = tk.Text(frMeasurement, width=10, height=8)
            txMeasurement.pack(side="left")
            scbMeasurement.pack(side="left", fill="y")

            # Anzeige und Scrollbar Anleitung
            lbRecipe = tk.Label(recipe_view, text="Anleitung:")
            lbRecipe.place(x=10, y=230)
            frRecipe = tk.Frame(recipe_view)
            frRecipe.place(x=90, y=230)
            scbRecipe = tk.Scrollbar(frRecipe, orient="vertical")
            txRecipe = tk.Text(
                frRecipe, width=58, height=12, yscrollcommand=scbRecipe.set
            )
            scbRecipe["command"] = txRecipe.yview
            txRecipe.pack(side="left")
            scbRecipe.pack(side="left", fill="y")

            # Rückgabewerte automatisch anzeigen
            categorie()
            time()
            name()
            ingredient()
            measurement()
            recipe()

            # Buttons erzeugen
            buPrint = tk.Button(recipe_view, text="Drucken",)
            buPrint.place(x=220, y=445)

            buClose = tk.Button(
                recipe_view, text="Schließen", command=recipe_view.destroy
            )
            buClose.place(x=420, y=445)
        # TODO zum Essensplan hinzufügen
        elif args == 32:
            """zu Essensplan."""
            # Fenster erzeugen
            recipe_add = Toplevel()
            recipe_add.title(config.sidebar_buttons[6][1][0])
            recipe_add.geometry("+%d+%d" % (400, 200))

            # Auswahl Woche
            recipe_thisweek = Radiobutton(
                recipe_add, text="Aktuelle Woche", indicatoron=0
            ).grid(column=1, row=1)
            recipe_nextweek = Radiobutton(
                recipe_add, text="Nächste Woche", indicatoron=0, value=0
            ).grid(column=2, row=1)

            # Auswahl Wochentag
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
        # ANCHOR neue Kategorie
        elif args == 33:
            """neue Kategorie."""
            # Fenster erzeugen
            categorie_new = Toplevel()
            categorie_new.title(config.sidebar_buttons[6][2][0])
            categorie_new.geometry("+%d+%d" % (400, 200))

            # Eingabe in Variable speichern
            cat_new = StringVar()

            # neue Kategorie in Datenbank schreiben
            def commit():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute("SELECT max(id_categorie) FROM rec_cat")
                max_id = cursor.fetchone()[-1]
                new_categorie = cat_new.get()
                iD = int(max_id) + 1
                Dir = "dir" + str((max_id + 2))
                Sub1 = "dir " + str((max_id + 2))
                Sub2 = "dir  " + str((max_id + 2))
                cursor.execute(
                    "INSERT INTO rec_cat(id_categorie, categorie, dir, sub1, sub2) VALUES(?, ?, ?, ?, ?)",
                    (iD, new_categorie, Dir, Sub1, Sub2),
                )
                con.commit()
                cursor.close()
                con.close()
                categorie_new.destroy()

            # neue Kategorie dynamisch in Tree einfügen
            def refresh():
                tree.insert("", "end", cat_new.get(), text=cat_new.get())

            # bei Bestätigung mit Enter
            def entry_return(event):
                commit()
                refresh()

            # Anzeige "Neue Kategorie"
            cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:")
            cat_new_label.grid(column=1, row=1)

            cat_new_entry = tk.Entry(categorie_new, textvariable=cat_new)
            cat_new_entry.grid(column=2, row=1)
            cat_new_entry.focus()
            cat_new_entry.bind("<Return>", entry_return)

            # Buttons erzeugen
            cat_new_button1 = tk.Button(
                categorie_new, text="OK", command=lambda: [commit(), refresh()]
            )
            cat_new_button1.grid(column=1, row=2)
            cat_new_button2 = tk.Button(
                categorie_new, text="Abbrechen", command=categorie_new.destroy
            )
            cat_new_button2.grid(column=2, row=2)
        # ANCHOR neues Rezept
        elif args == 34:
            """Neues Rezept."""
            # Fenster erzeugen
            recipe_new = Toplevel()
            recipe_new.title(config.sidebar_buttons[6][0][0])
            recipe_new.geometry("+%d+%d" % (250, 50))
            recipe_new["height"] = 480
            recipe_new["width"] = 600

            # Eingaben in Variablen speichern
            Name = StringVar()
            Categorie = StringVar()
            Time = StringVar()

            # Rezept in Datenbank schreiben
            def commit():
                global cat
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute("SELECT max(id_recipe) FROM rec_recipe")
                max_id = cursor.fetchone()[-1]
                index = int(max_id) + 1
                meal = ""
                name = Name.get()
                cat = Categorie.get()
                catList = []
                time = Time.get()
                Recipe = str(txRecipe.get(1.0, END))
                Ingredient = str(txIngredient.get(1.0, END))
                Measurement = str(txMeasurement.get(1.0, END))

                # Rezept in Datenbank schreiben
                cursor.execute(
                    "INSERT INTO rec_recipe(id_recipe, rec_categorie, name, recipe, ingredient, measurement, time, meal) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        index,
                        cat[2:-3],
                        name,
                        Recipe,
                        Ingredient,
                        Measurement,
                        time,
                        meal,
                    ),
                )
                catList.append(cat)
                con.commit()
                cursor.close()
                con.close()

                # Kategorie zum Einsetzen in Treeview auslesen
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT dir FROM rec_cat WHERE categorie LIKE ?",
                    ("%" + str(catList[0][2:-3]) + "%",),
                )
                cat_dir = cursor.fetchone()
                cursor.close()
                con.close()

                # Rezept dynamisch in Treeview einfügen
                tree.insert(cat_dir, "end", text=Name.get(), values=[Time.get()])
                recipe_new.destroy()

            # Scrollbarverknüpfung Zutaten und Mengen
            def multi_scrollbar(*args):
                txMeasurement.yview(*args)
                txIngredient.yview(*args)

            # Dropdown Menü Einträge
            OptionList = config.recipe[16]
            timeList = config.recipe[15]

            option = tk.StringVar()
            option.set(OptionList[0])

            timing = tk.StringVar()
            timing.set(timeList[0])

            # Anzeige Name
            lbName = tk.Label(recipe_new, text="Rezept:")
            lbName.place(x=10, y=10)
            txName = tk.Entry(recipe_new, textvariable=Name, width=55)
            txName.place(x=90, y=10)
            txName.focus()

            # Anzeige Kategorie
            lbCategorie = tk.Label(recipe_new, text="Kategorie:")
            lbCategorie.place(x=10, y=40)
            txCategorie = tk.OptionMenu(recipe_new, Categorie, *OptionList)
            txCategorie.place(x=90, y=35)

            # Anzeige Dauer
            lbTime = tk.Label(recipe_new, text="Dauer:")
            lbTime.place(x=220, y=40)
            txTime = tk.OptionMenu(recipe_new, Time, *timeList)
            txTime.place(x=270, y=35)

            # Anzeige und Scrollbar Zutaten
            lbIngredient = tk.Label(recipe_new, text="Zutaten:")
            lbIngredient.place(x=10, y=70)
            frIngredient = tk.Frame(recipe_new)
            frIngredient.place(x=90, y=70)
            scbIngredient = tk.Scrollbar(
                frIngredient, orient="vertical", command=multi_scrollbar
            )
            txIngredient = tk.Text(
                frIngredient, width=36, height=8, yscrollcommand=scbIngredient.set,
            )
            scbIngredient["command"] = txIngredient.yview
            txIngredient.pack(side="left")
            scbIngredient.pack(side="left", fill="y")

            # Anzeige und Scrollbar Mengen
            lbMeasurement = tk.Label(recipe_new, text="Menge:")
            lbMeasurement.place(x=410, y=70)
            frMeasurement = tk.Frame(recipe_new)
            frMeasurement.place(x=475, y=70)
            scbMeasurement = tk.Scrollbar(
                frMeasurement, orient="vertical", command=multi_scrollbar
            )
            txMeasurement = tk.Text(
                frMeasurement, width=10, height=8, yscrollcommand=scbMeasurement.set
            )
            scbMeasurement["command"] = txMeasurement.yview
            txMeasurement.pack(side="left")
            scbMeasurement.pack(side="left", fill="y")

            # Anzeige und Scrollbar Anleitung
            lbRecipe = tk.Label(recipe_new, text="Anleitung:")
            lbRecipe.place(x=10, y=230)
            frRecipe = tk.Frame(recipe_new)
            frRecipe.place(x=90, y=230)
            scbRecipe = tk.Scrollbar(frRecipe, orient="vertical")
            txRecipe = tk.Text(
                frRecipe, width=58, height=12, yscrollcommand=scbRecipe.set
            )
            scbRecipe["command"] = txRecipe.yview
            txRecipe.pack(side="left")
            scbRecipe.pack(side="left", fill="y")

            # Untere Buttons
            buSave = tk.Button(recipe_new, text="Speichern", command=lambda: [commit()])
            buSave.place(x=220, y=445)

            buClose = tk.Button(
                recipe_new, text="Schließen", command=recipe_new.destroy
            )
            buClose.place(x=420, y=445)
        # TODO Rezept ändern
        elif args == 35:
            """Rezept ändern."""
            # Fenster erzeugen
            recipe_edit = Toplevel()
            recipe_edit.title(config.sidebar_buttons[6][0][0])
            recipe_edit.geometry("+%d+%d" % (250, 50))
            recipe_edit["height"] = 480
            recipe_edit["width"] = 600

            # Eingabe in Variable speichern
            Name = StringVar()
            Categorie = StringVar()
            Time = StringVar()

            # Rezept in Datenbank schreiben
            def commit():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute("SELECT max(id_recipe) FROM rec_recipe")
                max_id = cursor.fetchone()[-1]
                index = int(max_id) + 1
                meal = ""
                name = Name.get()
                cat = Categorie.get()
                time = Time.get()
                Recipe = str(txRecipe.get(1.0, END))
                Ingredient = str(txIngredient.get(1.0, END))
                Measurement = str(txMeasurement.get(1.0, END))
                cursor.execute(
                    "INSERT INTO rec_recipe(id_recipe, rec_categorie, name, recipe, ingredient, measurement, time, meal) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        index,
                        cat[2:-3],
                        name,
                        Recipe,
                        Ingredient,
                        Measurement,
                        time,
                        meal,
                    ),
                )
                con.commit()
                cursor.close()
                con.close()
                recipe_edit.destroy()

            # Kategorie auslesen
            def categorie():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT rec_categorie FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    Categorie.set(dsatz)
                con.close()

            # Dauer auslesen
            def time():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT time FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    Time.set(dsatz)
                con.close()

            # Name auslesen
            def name():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT name FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    txName.insert("end", dsatz[0])
                con.close()

            # Zutaten auslesen
            def ingredient():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT ingredient FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    txIngredient.insert("end", dsatz[0])
                con.close()

            # Mengen auslesen
            def measurement():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT measurement FROM rec_recipe WHERE name = ?",
                    (selection_rec,),
                )
                for dsatz in cursor:
                    txMeasurement.insert("end", dsatz[0])

                con.close()

            # Anleitung auslesen
            def recipe():
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT recipe FROM rec_recipe WHERE name = ?", (selection_rec,),
                )
                for dsatz in cursor:
                    txRecipe.insert("end", dsatz[0])
                con.close()

            # Scrollbarverknüpfung Zutaten und Mengen
            def multi_scrollbar(*args):
                txMeasurement.yview(*args)
                txMeasurement.configure(yscrollcommand=scbMeasurement.set)
                txIngredient.yview(*args)
                txIngredient.configure(yscrollcommand=scbIngredient.set)

            # Dropdown Menü Einträge
            OptionList = config.recipe[16]
            timeList = config.recipe[15]

            option = tk.StringVar()
            option.set(OptionList[0])

            timing = tk.StringVar()
            timing.set(timeList[0])

            # Anzeige Name
            lbName = tk.Label(recipe_edit, text="Rezept:")
            lbName.place(x=10, y=10)
            txName = tk.Entry(recipe_edit, textvariable=Name, width=55)
            txName.place(x=90, y=10)
            txName.focus()

            # Anzeige Kategorie
            lbCategorie = tk.Label(recipe_edit, text="Kategorie:")
            lbCategorie.place(x=10, y=40)
            txCategorie = tk.OptionMenu(recipe_edit, Categorie, *OptionList)
            txCategorie.place(x=90, y=35)

            # Anzeige Dauer
            lbTime = tk.Label(recipe_edit, text="Dauer:")
            lbTime.place(x=220, y=40)
            txTime = tk.OptionMenu(recipe_edit, Time, *timeList)
            txTime.place(x=270, y=35)

            # Anzeige und Scrollbar Zutaten
            lbIngredient = tk.Label(recipe_edit, text="Zutaten:")
            lbIngredient.place(x=10, y=70)
            frIngredient = tk.Frame(recipe_edit)
            frIngredient.place(x=90, y=70)
            scbIngredient = tk.Scrollbar(
                frIngredient, orient="vertical", command=multi_scrollbar
            )
            txIngredient = tk.Text(
                frIngredient, width=36, height=8, yscrollcommand=scbIngredient.set,
            )
            scbIngredient["command"] = txIngredient.yview
            txIngredient.pack(side="left")
            scbIngredient.pack(side="left", fill="y")

            # Anzeige und Scrollbar Mengen
            lbMeasurement = tk.Label(recipe_edit, text="Menge:")
            lbMeasurement.place(x=410, y=70)
            frMeasurement = tk.Frame(recipe_edit)
            frMeasurement.place(x=475, y=70)
            scbMeasurement = tk.Scrollbar(
                frMeasurement, orient="vertical", command=multi_scrollbar
            )
            txMeasurement = tk.Text(
                frMeasurement, width=10, height=8, yscrollcommand=scbMeasurement.set
            )
            scbMeasurement["command"] = txMeasurement.yview
            txMeasurement.pack(side="left")
            scbMeasurement.pack(side="left", fill="y")

            # Anzeige und Scrollbar Anleitung
            lbRecipe = tk.Label(recipe_edit, text="Anleitung:")
            lbRecipe.place(x=10, y=230)
            frRecipe = tk.Frame(recipe_edit)
            frRecipe.place(x=90, y=230)
            scbRecipe = tk.Scrollbar(frRecipe, orient="vertical")
            txRecipe = tk.Text(
                frRecipe, width=58, height=12, yscrollcommand=scbRecipe.set
            )
            scbRecipe["command"] = txRecipe.yview
            txRecipe.pack(side="left")
            scbRecipe.pack(side="left", fill="y")

            # Rückgabewerte automatisch anzeigen
            categorie()
            time()
            name()
            ingredient()
            measurement()
            recipe()

            # Buttons erzeugen
            buSave = tk.Button(recipe_edit, text="Speichern", command=commit)
            buSave.place(x=220, y=445)

            buClose = tk.Button(
                recipe_edit, text="Schließen", command=recipe_edit.destroy
            )
            buClose.place(x=420, y=445)
        # ANCHOR Rezept löschen
        elif args == 36:
            """Rezept löschen."""
            # Messagebox mit Ja/Nein erzeugen
            recipe_del = tk.messagebox.askquestion(
                config.sidebar_buttons[6][5][0],
                "Möchtest du das Rezept\n '" + selection_rec + "'\n wirklich löschen?",
                icon="warning",
            )

            # Ausgewähltes Rezept aus Datenbank löschen
            if recipe_del == "yes":
                con = sqlite3.connect("family_data.db")
                cursor = con.cursor()
                cursor.execute(
                    "DELETE FROM rec_recipe WHERE name = ?", (selection_rec,)
                )
                con.commit()
                cursor.close()
                con.close()

                # Ausgewähltes Rezept aus Tree löschen
                selected_items = tree.selection()
                for selected_item in selected_items:
                    tree.delete(selected_item)
    # SECTION Meal
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
    # SECTION Household
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

