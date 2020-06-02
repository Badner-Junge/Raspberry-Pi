"""FamiliyOrganizer Modules.

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

# Tabs und Inhalt erzeugen und verwalten
class Tabs:
    """Manage Tabs."""

    def cards(self):
        """Create Tabs."""
        tabControl = ttk.Notebook(self, style="main.TNotebook")

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht    ")
        Tabs.uebersicht(self)
        # print(tabControl.index(tabControl.select()))

        self.tab7 = ttk.Frame(tabControl)
        tabControl.add(self.tab7, text="To-Do          ")
        Tabs.to_do(self)

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Kinder         ")
        Tabs.kinder(self)
        # print(tabControl.tab(tabControl.select(), "text"))

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Kalender     ")
        Tabs.kalender(self)

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Einkaufen   ")
        Tabs.einkaufen(self)

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Rezepte      ")
        Tabs.rezepte(self)

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Essensplan ")
        Tabs.essensplan(self)

        self.tab8 = ttk.Frame(tabControl)
        tabControl.add(self.tab8, text="Haushalt     ")
        Tabs.haushalt(self)

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl

    def uebersicht(self):
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

    def to_do(self):
        """Tab7."""
        Label(self.tab7, text="Please Select your choice").place(x=250, y=80)

    def kinder(self):
        """Tab2."""
        kids_frame = tk.Frame(self.tab2)
        kids_frame.pack(fill="both")

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

    def kalender(self):
        """Tab3 Calendar."""
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
            "meeting", background=config.calendar[0], foreground=config.calendar[1]
        )
        cal.pack(side="left", fill="both", expand=True)

        """Tab3 Buttons."""
        cal_frame_buttons = tk.Frame(self.tab3)
        cal_frame_buttons.pack(anchor="e", fill="y", expand=1)

        cal_button1 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][0],
            bg=config.calendar[3][0],
            command=lambda: cal_top_window(1),
        )
        cal_button1.pack(anchor="e", fill="both", expand=1)

        cal_button2 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][1],
            bg=config.calendar[3][1],
            command=lambda: cal_top_window(2),
        )
        cal_button2.pack(anchor="e", fill="both", expand=1)

        cal_button3 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][2],
            bg=config.calendar[3][2],
            command=lambda: cal_top_window(3),
        )
        cal_button3.pack(anchor="e", fill="both", expand=1)

        cal_button4 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][3],
            bg=config.calendar[3][3],
            command=lambda: cal_top_window(4),
        )
        cal_button4.pack(anchor="e", fill="both", expand=1)

        cal_button5 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][4],
            bg=config.calendar[3][4],
            command=lambda: cal_top_window(5),
        )
        cal_button5.pack(anchor="e", fill="both", expand=1)

        cal_button6 = tk.Button(
            cal_frame_buttons,
            text=config.calendar[2][5],
            bg=config.calendar[3][5],
            command=lambda: cal_top_window(6),
        )
        cal_button6.pack(anchor="e", fill="both", expand=1)

        print("Kalender:", config.calendar)

    def einkaufen(self):
        """Tab4."""
        Label(self.tab4, text="Please Select your choice").place(x=250, y=80)

    def rezepte(self):
        """Tab5 Treeview."""
        tree = ttk.Treeview(self.tab5, columns=("one", "two"))
        # tree["columns"] = ("one", "two")
        tree.column("one", width=config.recipe[0][0])
        tree.column("two", width=config.recipe[1][0])
        tree.heading("one", text=config.recipe[0][1])
        tree.heading("two", text=config.recipe[1][1])

        cat1 = tree.insert("", 1, "dir2", text=config.recipe[2][0])
        tree.insert(
            cat1, "end", "dir 2", text=config.recipe[0][2], values=(config.recipe[0][3])
        )

        cat2 = tree.insert("", 2, "dir3", text=config.recipe[2][1])
        tree.insert(
            cat2, "end", "dir 3", text=config.recipe[1][2], values=(config.recipe[1][3])
        )

        tree.pack(side="left", anchor="nw", fill="both", expand=True)

        """Tab5 Buttons."""
        rec_frame_buttons = tk.Frame(self.tab5)
        rec_frame_buttons.pack(anchor="e", fill="y", expand=1)

        # Rezept anzeigen
        rec_button1 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][0],
            text=config.recipe[3][0],
            command=lambda: rec_top_window(1),
        )
        rec_button1.pack(anchor="e", fill="both", expand=1)

        # zum Essensolan
        rec_button2 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][1],
            text=config.recipe[3][1],
            command=lambda: rec_top_window(2),
        )
        rec_button2.pack(anchor="e", fill="both", expand=1)

        # neue Kategorie
        rec_button3 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][2],
            text=config.recipe[3][2],
            command=lambda: rec_top_window(3),
        )
        rec_button3.pack(anchor="e", fill="both", expand=1)

        # neues Rezept
        rec_button4 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][3],
            text=config.recipe[3][3],
            command=lambda: rec_top_window(4),
        )
        rec_button4.pack(anchor="e", fill="both", expand=1)

        # Rezept bearbeiten
        rec_button5 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][4],
            text=config.recipe[3][4],
            command=lambda: rec_top_window(5),
        )
        rec_button5.pack(anchor="e", fill="both", expand=1)

        # Rezept löschen
        rec_button6 = tk.Button(
            rec_frame_buttons,
            bg=config.recipe[4][5],
            text=config.recipe[3][5],
            command=lambda: rec_top_window(6),
        )
        rec_button6.pack(anchor="e", fill="both", expand=1)

    def essensplan(self):
        """Tab6 Days."""
        day_frame = tk.Frame(self.tab6)
        day_frame.pack(side="left", fill="both", expand=True)
        Label1 = Label(
            day_frame, text="Wochentag", bd=5, relief="sunken", font="Times 24 bold"
        ).pack()

        for txt in config.meal[1]:
            Label(day_frame, text=txt, font="Times 24").pack(fill="y", expand=True)

        """Tab6 Frame this week."""
        this_week_frame = tk.Frame(self.tab6)
        this_week_frame.pack(side="left", fill="both", expand=True)
        Label2 = Label(
            this_week_frame,
            text="aktuelle Woche",
            bd=5,
            relief="sunken",
            font="Times 24 bold",
        ).pack()

        for txt in config.meal[1]:
            Entry(this_week_frame, text=txt, font="Times 18").pack(
                fill="y", expand=True
            )

        """Tab6 Frame next week."""
        next_week_frame = tk.Frame(self.tab6)
        next_week_frame.pack(side="left", fill="both", expand=True)
        Label3 = Label(
            next_week_frame,
            text="nächste Woche",
            bd=5,
            relief="sunken",
            font="Times 24 bold",
        ).pack()

        for txt in config.meal[1]:
            Entry(next_week_frame, text=txt, font="Times 18").pack(
                fill="y", expand=True
            )

        """Tab6 Buttons."""
        meal_frame_buttons = tk.Frame(self.tab6)
        meal_frame_buttons.pack(anchor="e", fill="y", expand=1)

        # Rezept anzeigen
        meal_button1 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][0],
            text=config.meal[2][0],
            command=lambda: meal_top_window(1),
        )
        meal_button1.pack(anchor="e", fill="both", expand=1)

        # zum Essensolan
        meal_button2 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][1],
            text=config.meal[2][1],
            command=lambda: meal_top_window(2),
        )
        meal_button2.pack(anchor="e", fill="both", expand=1)

        # neue Kategorie
        meal_button3 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][2],
            text=config.meal[2][2],
            command=lambda: meal_top_window(3),
        )
        meal_button3.pack(anchor="e", fill="both", expand=1)

        # neues Rezept
        meal_button4 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][3],
            text=config.meal[2][3],
            command=lambda: meal_top_window(4),
        )
        meal_button4.pack(anchor="e", fill="both", expand=1)

        # Rezept bearbeiten
        meal_button5 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][4],
            text=config.meal[2][4],
            command=lambda: meal_top_window(5),
        )
        meal_button5.pack(anchor="e", fill="both", expand=1)

        # Rezept löschen
        meal_button6 = tk.Button(
            meal_frame_buttons,
            bg=config.meal[3][5],
            text=config.meal[2][5],
            command=lambda: meal_top_window(6),
        )
        meal_button6.pack(anchor="e", fill="both", expand=1)

    def haushalt(self):
        """Tab8."""
        Label(self.tab8, text="Please Select your choice").place(x=250, y=80)


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


# Optionen Menü
def fullscreen_toggle(self):
    """Switch Fullscreen on/off."""
    if self.attributes("-fullscreen") == FALSE:
        self.attributes("-fullscreen", TRUE)
    else:
        self.attributes("-fullscreen", FALSE)
