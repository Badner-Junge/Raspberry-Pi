"""FamiliyOrganizer Modules.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from test_config import *
import test_config, datetime, tkcalendar, tkinter.messagebox
import tkinter as tk

# Tabs und Inhalt erzeugen und verwalten
class Tabs:
    """Manage Tabs."""

    def cards(self):
        # Button Sidebar
        def sidebar(self):
            frame_sidebar = tk.Frame(self.tab1)
            frame_sidebar.pack(side="left", anchor="e", fill="y", expand=1)

            button1 = tk.Button(
                frame_sidebar,
                text=test_config.sidebar_config[0][0],
                bg=test_config.sidebar_config[0][1],
                width=14,
            )
            button1.pack(anchor="e", fill="y", expand=1)

        # Create Tabs
        tabControl = ttk.Notebook(self, style="main.TNotebook")

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht")
        Tabs.overview(self)

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
        Tabs.meal(self)

        self.tab8 = ttk.Frame(tabControl)
        tabControl.add(self.tab8, text="Hahabu")
        Tabs.household(self)

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl

        sidebar(self)
        # tabControl = [print(tabControl.index(tabControl.select()))]
        # return tabControl
        # print(tabControl)

    def overview(self):
        """Tab1 Übersicht."""

    def to_do(self):
        """Tab2 To-Do."""
        # print(Tabs.cards.tabControl.index(tabControl.select()))

    def kids(self):
        """Tab3 Kinder Register."""
        kids_frame = tk.Frame(self.tab2)
        kids_frame.pack(side="left", anchor="n", fill="both", expand=1)

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

        # print(tabControl.index(tabControl.select()))

    def calendar(self):
        """Tab4 Kalender."""
        events = {
            "2020-06-28": ("London", "meeting"),
            "2020-06-15": ("Paris", "meeting"),
            "2020-06-30": ("New York", "meeting"),
        }
        cal = Calendar(self.tab3, selectmode="day")

        for k in events.keys():
            date = datetime.datetime.strptime(k, "%Y-%m-%d").date()
            cal.calevent_create(date, events[k][0], events[k][1])

        cal.tag_config(
            "meeting",
            background=test_config.calendar_config[0],
            foreground=test_config.calendar_config[1],
        )
        cal.pack(side="left", fill="both", expand=True)

    def shopping(self):
        """Tab5 Einkaufen."""

    def recipes(self):
        """Tab6 Rezepte."""
        tree = ttk.Treeview(self.tab5, columns=("one", "two"))
        # tree["columns"] = ("one", "two")
        tree.column("one", width=test_config.recipes_config[0][0])
        tree.column("two", width=test_config.recipes_config[1][0])
        tree.heading("one", text=test_config.recipes_config[0][1])
        tree.heading("two", text=test_config.recipes_config[1][1])

        cat1 = tree.insert("", 1, "dir2", text=test_config.recipes_config[2][0])
        tree.insert(
            cat1,
            "end",
            "dir 2",
            text=test_config.recipes_config[0][2],
            values=(test_config.recipes_config[0][3]),
        )

        cat2 = tree.insert("", 2, "dir3", text=test_config.recipes_config[2][1])
        tree.insert(
            cat2,
            "end",
            "dir 3",
            text=test_config.recipes_config[1][2],
            values=(test_config.recipes_config[1][3]),
        )

        tree.pack(side="left", anchor="nw", fill="both", expand=True)

    def meal(self):
        """Tab7 Essensplan."""
        v = IntVar()
        v.set(0)

        day_frame = tk.Frame(self.tab6)
        day_frame.pack(side="left", fill="both", expand=True)
        Label1 = Label(
            day_frame, text="Wochentag", bd=5, relief="sunken", font="Times 24 bold"
        ).pack()

        for txt in test_config.meal_config[1]:
            Label(day_frame, text=txt, font="Times 24").pack(fill="y", expand=True)

    def household(self):
        """Tab8 Haushalt."""
        Label(self.tab8, text="Please Select your choice").place(x=250, y=80)


def view_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Essen hinzufügen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][0])
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
        print(config.todo[0][0])
    elif args == 2:
        """Essen ändern."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][1])
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
        print(config.todo[0][1])
    elif args == 3:
        """?."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][2])
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
        print(config.todo[0][2])
    elif args == 4:
        """Einzelnen Tag löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][3])
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
        print(config.todo[0][3])
    elif args == 5:
        """Woche 1 löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][4])
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
        print(config.todo[0][4])
    elif args == 6:
        """Woche 2 löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][5])
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
        print(config.todo[0][5])


def todo_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Essen hinzufügen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][0])
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
        print(config.todo[0][0])
    elif args == 2:
        """Essen ändern."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][1])
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
        print(config.todo[0][1])
    elif args == 3:
        """?."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][2])
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
        print(config.todo[0][2])
    elif args == 4:
        """Einzelnen Tag löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][3])
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
        print(config.todo[0][3])
    elif args == 5:
        """Woche 1 löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][4])
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
        print(config.todo[0][4])
    elif args == 6:
        """Woche 2 löschen."""
        todo_add = Toplevel()
        todo_add.title(config.todo[0][5])
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
        print(config.todo[0][5])


def kids_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Essen hinzufügen."""
        kids_add = Toplevel()
        kids_add.title(config.kids[0][0])
        kids_add.geometry("+%d+%d" % (400, 200))
        kids_add_label1 = tk.Label(kids_add, text="Rezept:").grid(column=1, row=1)
        kids_add_label2 = tk.Label(kids_add, text="Zutaten:").grid(column=1, row=2)
        kids_add_label3 = tk.Label(kids_add, text="Anleitung:").grid(column=1, row=3)

        kids_add_entry1 = tk.Entry(kids_add).grid(column=2, row=1)
        kids_add_entry2 = tk.Entry(kids_add).grid(column=2, row=2)
        kids_add_entry3 = tk.Entry(kids_add).grid(column=2, row=3)

        kids_add_button1 = tk.Button(kids_add, text="OK").grid(column=1, row=4)
        kids_add_button2 = tk.Button(
            kids_add, text="Abbrechen", command=kids_add.destroy
        ).grid(column=2, row=4)
        print(config.kids[0][0])
    elif args == 2:
        """Essen ändern."""
        kids_edit = Toplevel()
        kids_edit.title(config.kids[0][1])
        kids_edit.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(kids_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

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
        print(config.kids[0][1])
    elif args == 3:
        """?."""
        kids_del = Toplevel()
        kids_del.title(config.kids[0][2])
        kids_del.geometry("+%d+%d" % (400, 200))
        kids_del_label = tk.Label(kids_del, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        kids_del_entry = tk.Entry(kids_del).grid(column=2, row=1)
        kids_del_button1 = tk.Button(kids_del, text="OK").grid(column=1, row=2)
        kids_del_button2 = tk.Button(
            kids_del, text="Abbrechen", command=kids_del.destroy
        ).grid(column=2, row=2)
        print(config.kids[0][2])
    elif args == 4:
        """Einzelnen Tag löschen."""
        kids_del = tk.messagebox.askquestion(
            config.kids[0][3],
            "Möchtest du einen Tag wirklich löschen?",
            icon="warning",
        )
        if kids_del == "yes":
            print("Ein Tag gelöscht")
        else:
            print("Ein Tag nicht gelöscht")
        print(config.kids[0][3])
    elif args == 5:
        """Woche 1 löschen."""
        kids_del = tk.messagebox.askquestion(
            config.kids[0][4], "Möchtest du Woche 1 wirklich löschen?", icon="warning",
        )
        if kids_del == "yes":
            print("Woche 1 gelöscht")
        else:
            print("Woche 1 nicht gelöscht")
        print(config.kids[0][4])
    elif args == 6:
        """Woche 2 löschen."""
        kids_del = tk.messagebox.askquestion(
            config.kids[0][5], "Möchtest du Woche 2 wirklich löschen?", icon="warning",
        )
        if kids_del == "yes":
            print("Woche 2 gelöscht")
        else:
            print("Woche 2 nicht gelöscht")
        print(config.kids[0][5])


def cal_top_window(args):
    """Create Toplevel Windows Kalender."""
    if args == 1:
        """zu Essensplan."""
        cal_view = Toplevel()
        cal_view.title(config.calendar[2][0])
        cal_view.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(cal_view, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

        for txt, val in config.meal:
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
        print(config.calendar[2][0])
    elif args == 2:
        """neue Kategorie."""
        categorie_new = Toplevel()
        categorie_new.title(config.calendar[2][1])
        categorie_new.geometry("+%d+%d" % (400, 200))
        cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
        cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
        cat_new_button2 = tk.Button(
            categorie_new, text="Abbrechen", command=categorie_new.destroy
        ).grid(column=2, row=2)
        print(config.calendar[2][1])
    elif args == 3:
        """neues Rezept."""
        recipe_new = Toplevel()
        recipe_new.title(config.calendar[2][2])
        recipe_new.geometry("+%d+%d" % (400, 200))
        rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
            column=1, row=1
        )
        rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
        rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(column=1, row=3)

        rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

        rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
        rec_new_button2 = tk.Button(
            recipe_new, text="Abbrechen", command=recipe_new.destroy
        ).grid(column=2, row=4)
        print(config.calendar[2][2])
    elif args == 4:
        """Rezept ändern."""
        recipe_edit = Toplevel()
        recipe_edit.title(config.calendar[2][3])
        recipe_edit.geometry("+%d+%d" % (400, 200))
        rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(column=1, row=1)
        rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(column=1, row=2)
        rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(column=1, row=3)

        rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
        rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
        rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

        rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
        rec_edit_button2 = tk.Button(
            recipe_edit, text="Abbrechen", command=recipe_edit.destroy
        ).grid(column=2, row=4)
        print(config.calendar[2][3])
    elif args == 5:
        """Rezept ändern."""
        recipe_edit = Toplevel()
        recipe_edit.title(config.calendar[2][4])
        recipe_edit.geometry("+%d+%d" % (400, 200))
        rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(column=1, row=1)
        rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(column=1, row=2)
        rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(column=1, row=3)

        rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
        rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
        rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

        rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
        rec_edit_button2 = tk.Button(
            recipe_edit, text="Abbrechen", command=recipe_edit.destroy
        ).grid(column=2, row=4)
        print(config.calendar[2][4])
    elif args == 6:
        """Rezept löschen."""
        recipe_del = tk.messagebox.askquestion(
            config.calendar[2][5],
            "Möchtest du den Termin wirklich löschen?",
            icon="warning",
        )
        if recipe_del == "yes":
            print("Termin gelöscht")
        else:
            print("Termin nicht gelöscht")
        print(config.calendar[2][5])


def shop_top_window(args):
    """Create Toplevel Windows Einkaufen."""
    if args == 1:
        """Rezept anzeigen."""
        recipe_view = Toplevel()
        recipe_view.title(config.buy[3][0])
        recipe_view.geometry("+%d+%d" % (400, 200))
        rec_view_label1 = tk.Label(recipe_view, text="Rezept:").grid(column=1, row=1)
        rec_view_label2 = tk.Label(recipe_view, text="Zutaten:").grid(column=1, row=2)
        rec_view_label3 = tk.Label(recipe_view, text="Anleitung:").grid(column=1, row=3)

        rec_view_entry1 = tk.Entry(recipe_view).grid(column=2, row=1)
        rec_view_entry2 = tk.Entry(recipe_view).grid(column=2, row=2)
        rec_view_entry3 = tk.Entry(recipe_view).grid(column=2, row=3)

        rec_view_button1 = tk.Button(recipe_view, text="OK").grid(column=1, row=4)
        rec_view_button2 = tk.Button(
            recipe_view, text="Abbrechen", command=recipe_view.destroy
        ).grid(column=2, row=4)
        print(config.buy[3][0])
    elif args == 2:
        """zu Essensplan."""
        recipe_add = Toplevel()
        recipe_add.title(config.buy[3][1])
        recipe_add.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(recipe_add, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

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
        print(config.buy[3][1])
    elif args == 3:
        """neue Kategorie."""
        categorie_new = Toplevel()
        categorie_new.title(config.buy[3][2])
        categorie_new.geometry("+%d+%d" % (400, 200))
        cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
        cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
        cat_new_button2 = tk.Button(
            categorie_new, text="Abbrechen", command=categorie_new.destroy
        ).grid(column=2, row=2)
        print(config.buy[3][2])
    elif args == 4:
        """neues Rezept."""
        recipe_new = Toplevel()
        recipe_new.title(config.buy[3][3])
        recipe_new.geometry("+%d+%d" % (400, 200))
        rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
            column=1, row=1
        )
        rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
        rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(column=1, row=3)

        rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

        rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
        rec_new_button2 = tk.Button(
            recipe_new, text="Abbrechen", command=recipe_new.destroy
        ).grid(column=2, row=4)
        print(config.buy[3][3])
    elif args == 5:
        """Rezept ändern."""
        recipe_edit = Toplevel()
        recipe_edit.title(config.buy[3][4])
        recipe_edit.geometry("+%d+%d" % (400, 200))
        rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(column=1, row=1)
        rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(column=1, row=2)
        rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(column=1, row=3)

        rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
        rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
        rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

        rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
        rec_edit_button2 = tk.Button(
            recipe_edit, text="Abbrechen", command=recipe_edit.destroy
        ).grid(column=2, row=4)
        print(config.buy[3][4])
    elif args == 6:
        """Rezept löschen."""
        recipe_del = tk.messagebox.askquestion(
            config.buy[3][5],
            "Möchtest du das Rezept wirklich löschen?",
            icon="warning",
        )
        if recipe_del == "yes":
            print("Rezept gelöscht")
        else:
            print("Rezept nicht gelöscht")
        print(config.buy[3][5])


def rec_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Rezept anzeigen."""
        recipe_view = Toplevel()
        recipe_view.title(config.recipe[3][0])
        recipe_view.geometry("+%d+%d" % (400, 200))
        rec_view_label1 = tk.Label(recipe_view, text="Rezept:").grid(column=1, row=1)
        rec_view_label2 = tk.Label(recipe_view, text="Zutaten:").grid(column=1, row=2)
        rec_view_label3 = tk.Label(recipe_view, text="Anleitung:").grid(column=1, row=3)

        rec_view_entry1 = tk.Entry(recipe_view).grid(column=2, row=1)
        rec_view_entry2 = tk.Entry(recipe_view).grid(column=2, row=2)
        rec_view_entry3 = tk.Entry(recipe_view).grid(column=2, row=3)

        rec_view_button1 = tk.Button(recipe_view, text="OK").grid(column=1, row=4)
        rec_view_button2 = tk.Button(
            recipe_view, text="Abbrechen", command=recipe_view.destroy
        ).grid(column=2, row=4)
        print(config.recipe[3][0])
    elif args == 2:
        """zu Essensplan."""
        recipe_add = Toplevel()
        recipe_add.title(config.recipe[3][1])
        recipe_add.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(recipe_add, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

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
        print(config.recipe[3][1])
    elif args == 3:
        """neue Kategorie."""
        categorie_new = Toplevel()
        categorie_new.title(config.recipe[3][2])
        categorie_new.geometry("+%d+%d" % (400, 200))
        cat_new_label = tk.Label(categorie_new, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        cat_new_entry = tk.Entry(categorie_new).grid(column=2, row=1)
        cat_new_button1 = tk.Button(categorie_new, text="OK").grid(column=1, row=2)
        cat_new_button2 = tk.Button(
            categorie_new, text="Abbrechen", command=categorie_new.destroy
        ).grid(column=2, row=2)
        print(config.recipe[3][2])
    elif args == 4:
        """neues Rezept."""
        recipe_new = Toplevel()
        recipe_new.title(config.recipe[3][3])
        recipe_new.geometry("+%d+%d" % (400, 200))
        rec_new_label1 = tk.Label(recipe_new, text="Neues Rezept:").grid(
            column=1, row=1
        )
        rec_new_label2 = tk.Label(recipe_new, text="Zutaten:").grid(column=1, row=2)
        rec_new_label3 = tk.Label(recipe_new, text="Anleitung:").grid(column=1, row=3)

        rec_new_entry1 = tk.Entry(recipe_new).grid(column=2, row=1)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=2)
        rec_new_entry2 = tk.Entry(recipe_new).grid(column=2, row=3)

        rec_new_button1 = tk.Button(recipe_new, text="OK").grid(column=1, row=4)
        rec_new_button2 = tk.Button(
            recipe_new, text="Abbrechen", command=recipe_new.destroy
        ).grid(column=2, row=4)
        print(config.recipe[3][3])
    elif args == 5:
        """Rezept ändern."""
        recipe_edit = Toplevel()
        recipe_edit.title(config.recipe[3][4])
        recipe_edit.geometry("+%d+%d" % (400, 200))
        rec_edit_label1 = tk.Label(recipe_edit, text="Rezept:").grid(column=1, row=1)
        rec_edit_label2 = tk.Label(recipe_edit, text="Zutaten:").grid(column=1, row=2)
        rec_edit_label3 = tk.Label(recipe_edit, text="Anleitung:").grid(column=1, row=3)

        rec_edit_entry1 = tk.Entry(recipe_edit).grid(column=2, row=1)
        rec_edit_entry2 = tk.Entry(recipe_edit).grid(column=2, row=2)
        rec_edit_entry3 = tk.Entry(recipe_edit).grid(column=2, row=3)

        rec_edit_button1 = tk.Button(recipe_edit, text="OK").grid(column=1, row=4)
        rec_edit_button2 = tk.Button(
            recipe_edit, text="Abbrechen", command=recipe_edit.destroy
        ).grid(column=2, row=4)
        print(config.recipe[3][4])
    elif args == 6:
        """Rezept löschen."""
        recipe_del = tk.messagebox.askquestion(
            config.recipe[3][5],
            "Möchtest du das Rezept wirklich löschen?",
            icon="warning",
        )
        if recipe_del == "yes":
            print("Rezept gelöscht")
        else:
            print("Rezept nicht gelöscht")
        print(config.recipe[3][5])


def meal_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Essen hinzufügen."""
        meal_add = Toplevel()
        meal_add.title(config.meal[2][0])
        meal_add.geometry("+%d+%d" % (400, 200))
        meal_add_label1 = tk.Label(meal_add, text="Rezept:").grid(column=1, row=1)
        meal_add_label2 = tk.Label(meal_add, text="Zutaten:").grid(column=1, row=2)
        meal_add_label3 = tk.Label(meal_add, text="Anleitung:").grid(column=1, row=3)

        meal_add_entry1 = tk.Entry(meal_add).grid(column=2, row=1)
        meal_add_entry2 = tk.Entry(meal_add).grid(column=2, row=2)
        meal_add_entry3 = tk.Entry(meal_add).grid(column=2, row=3)

        meal_add_button1 = tk.Button(meal_add, text="OK").grid(column=1, row=4)
        meal_add_button2 = tk.Button(
            meal_add, text="Abbrechen", command=meal_add.destroy
        ).grid(column=2, row=4)
        print(config.meal[2][0])
    elif args == 2:
        """Essen ändern."""
        meal_edit = Toplevel()
        meal_edit.title(config.meal[2][1])
        meal_edit.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(meal_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

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
        print(config.meal[2][1])
    elif args == 3:
        """?."""
        meal_del = Toplevel()
        meal_del.title(config.meal[2][2])
        meal_del.geometry("+%d+%d" % (400, 200))
        meal_del_label = tk.Label(meal_del, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        meal_del_entry = tk.Entry(meal_del).grid(column=2, row=1)
        meal_del_button1 = tk.Button(meal_del, text="OK").grid(column=1, row=2)
        meal_del_button2 = tk.Button(
            meal_del, text="Abbrechen", command=meal_del.destroy
        ).grid(column=2, row=2)
        print(config.meal[2][2])
    elif args == 4:
        """Einzelnen Tag löschen."""
        day_del = tk.messagebox.askquestion(
            config.meal[2][3],
            "Möchtest du einen Tag wirklich löschen?",
            icon="warning",
        )
        if day_del == "yes":
            print("Ein Tag gelöscht")
        else:
            print("Ein Tag nicht gelöscht")
        print(config.meal[2][3])
    elif args == 5:
        """Woche 1 löschen."""
        week1_del = tk.messagebox.askquestion(
            config.meal[2][4], "Möchtest du Woche 1 wirklich löschen?", icon="warning",
        )
        if week1_del == "yes":
            print("Woche 1 gelöscht")
        else:
            print("Woche 1 nicht gelöscht")
        print(config.meal[2][4])
    elif args == 6:
        """Woche 2 löschen."""
        week2_del = tk.messagebox.askquestion(
            config.meal[2][5], "Möchtest du Woche 2 wirklich löschen?", icon="warning",
        )
        if week2_del == "yes":
            print("Woche 2 gelöscht")
        else:
            print("Woche 2 nicht gelöscht")
        print(config.meal[2][5])


def house_top_window(args):
    """Create Toplevel Windows Rezepte."""
    if args == 1:
        """Essen hinzufügen."""
        meal_add = Toplevel()
        meal_add.title(config.meal[2][0])
        meal_add.geometry("+%d+%d" % (400, 200))
        meal_add_label1 = tk.Label(meal_add, text="Rezept:").grid(column=1, row=1)
        meal_add_label2 = tk.Label(meal_add, text="Zutaten:").grid(column=1, row=2)
        meal_add_label3 = tk.Label(meal_add, text="Anleitung:").grid(column=1, row=3)

        meal_add_entry1 = tk.Entry(meal_add).grid(column=2, row=1)
        meal_add_entry2 = tk.Entry(meal_add).grid(column=2, row=2)
        meal_add_entry3 = tk.Entry(meal_add).grid(column=2, row=3)

        meal_add_button1 = tk.Button(meal_add, text="OK").grid(column=1, row=4)
        meal_add_button2 = tk.Button(
            meal_add, text="Abbrechen", command=meal_add.destroy
        ).grid(column=2, row=4)
        print(config.meal[2][0])
    elif args == 2:
        """Essen ändern."""
        meal_edit = Toplevel()
        meal_edit.title(config.meal[2][1])
        meal_edit.geometry("+%d+%d" % (400, 200))

        v = IntVar()
        v.set(1)

        Label(meal_edit, text="Wähle einen Wochentag:", justify=LEFT, padx=20,).pack()

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
        print(config.meal[2][1])
    elif args == 3:
        """?."""
        meal_del = Toplevel()
        meal_del.title(config.meal[2][2])
        meal_del.geometry("+%d+%d" % (400, 200))
        meal_del_label = tk.Label(meal_del, text="Neue Kategorie:").grid(
            column=1, row=1
        )
        meal_del_entry = tk.Entry(meal_del).grid(column=2, row=1)
        meal_del_button1 = tk.Button(meal_del, text="OK").grid(column=1, row=2)
        meal_del_button2 = tk.Button(
            meal_del, text="Abbrechen", command=meal_del.destroy
        ).grid(column=2, row=2)
        print(config.meal[2][2])
    elif args == 4:
        """Einzelnen Tag löschen."""
        day_del = tk.messagebox.askquestion(
            config.meal[2][3],
            "Möchtest du einen Tag wirklich löschen?",
            icon="warning",
        )
        if day_del == "yes":
            print("Ein Tag gelöscht")
        else:
            print("Ein Tag nicht gelöscht")
        print(config.meal[2][3])
    elif args == 5:
        """Woche 1 löschen."""
        week1_del = tk.messagebox.askquestion(
            config.meal[2][4], "Möchtest du Woche 1 wirklich löschen?", icon="warning",
        )
        if week1_del == "yes":
            print("Woche 1 gelöscht")
        else:
            print("Woche 1 nicht gelöscht")
        print(config.meal[2][4])
    elif args == 6:
        """Woche 2 löschen."""
        week2_del = tk.messagebox.askquestion(
            config.meal[2][5], "Möchtest du Woche 2 wirklich löschen?", icon="warning",
        )
        if week2_del == "yes":
            print("Woche 2 gelöscht")
        else:
            print("Woche 2 nicht gelöscht")
        print(config.meal[2][5])


def fullscreen_toggle(self):
    """Switch Fullscreen on/off."""
    if self.attributes("-fullscreen") == FALSE:
        self.attributes("-fullscreen", TRUE)
    else:
        self.attributes("-fullscreen", FALSE)
