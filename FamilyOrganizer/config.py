"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from modules import *
import modules, tkinter.messagebox, os, sqlite3
import tkinter as tk


def new_file():
    if not os.path.exists("family_data.db"):
        con = sqlite3.connect("family_data.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(id INTEGER PRIMARY KEY, deu TEXT, eng TEXT, fra TEXT)"
        cursor.execute(sql)
        startdaten = [
            ["suchen", "to look for", "chercher"],
            ["abkürzen", "to abbreviate", "raccourcir"],
            ["nützlich", "useful", "utile"],
            ["beraten", "to advise", "conseiller"],
            ["einfach", "easy", "simple"],
            ["ankündigen", "to announce", "annoncer"],
        ]
        for gruppe in startdaten:
            sql = (
                "INSERT INTO daten(deu, eng, fra) VALUES('"
                + gruppe[0]
                + "', '"
                + gruppe[1]
                + "', '"
                + gruppe[2]
                + "')"
            )
            print(sql)
            cursor.execute(sql)
            con.commit()
        con.close()


def style():
    """Config Style Tabs."""
    tabConfiguration = ttk.Style()
    tabConfiguration.configure(
        "main.TNotebook",
        tabposition="w",
        tabmargins=0,
        padding=0,
        background="lightgrey",
    )
    tabConfiguration.configure(
        "kids.TNotebook",
        tabposition="n",
        tabmargins=0,
        padding=5,
        background="lightgrey",
        fill="both",
        expand=True,
    )
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook.Tab", font="Comic 24", background="white")

    """Config Style Recipes."""
    treeStyle = ttk.Style()
    treeStyle.configure("Treeview", rowheight=50, font="Times 18")


def sidebar_buttons():
    """Config Sidebar Buttonname, Buttoncolor, Toplevel."""
    config_buttons = [14, "Times 12 bold"]  # width  # font, size

    view_buttons = [
        ("view1", "grey", lambda: top_window(1)),
        ("view2", "grey", lambda: top_window(2)),
        ("view3", "grey", lambda: top_window(3)),
        ("view4", "grey", lambda: top_window(4)),
        ("view5", "grey", lambda: top_window(5)),
        ("view6", "grey", lambda: top_window(6)),
    ]

    todo_buttons = [
        ("Katja", "green", lambda: top_window(7)),
        ("Fabian", "green", lambda: top_window(8)),
        ("Fabienne", "red", lambda: top_window(9)),
        ("Mio", "orange", lambda: top_window(10)),
        ("Mika", "yellow", lambda: top_window(11)),
        ("Jona", "beige", lambda: top_window(12)),
    ]

    kids_buttons = [
        ("Kinder 1", "purple", lambda: top_window(13)),
        ("Kinder 2", "white", lambda: top_window(14)),
        ("Kinder 3", "green", lambda: top_window(15)),
        ("Kinder 4", "orange", lambda: top_window(16)),
        ("Kinder 5", "pink", lambda: top_window(17)),
        ("Kinder 6", "brown", lambda: top_window(18)),
    ]

    calendar_buttons = [
        ("Terminübersicht", "yellow", lambda: top_window(19)),
        ("Termin anzeigen", "yellow", lambda: top_window(20)),
        ("Termin suchen", "yellow", lambda: top_window(21)),
        ("Termin ändern", "orange", lambda: top_window(22)),
        ("neuer Termin", "lightgreen", lambda: top_window(23)),
        ("Termin löschen", "red", lambda: top_window(24)),
    ]

    shopping_buttons = [
        ("Artikel hinzufügen", "lightgreen", lambda: top_window(25)),
        ("Rezept hinzufügen", "lightgreen", lambda: top_window(26)),
        ("Menge ändern", "orange", lambda: top_window(27)),
        ("Artikel löschen", "red", lambda: top_window(28)),
        ("Liste löschen", "red", lambda: top_window(29)),
        ("Drucken", "blue", lambda: top_window(30)),
    ]

    recipes_buttons = [
        ("Rezept anzeigen", "yellow", lambda: top_window(31)),
        ("zum Essensplan", "lightgreen", lambda: top_window(32)),
        ("neue Kategorie", "lightgreen", lambda: top_window(33)),
        ("neues Rezept", "lightgreen", lambda: top_window(34)),
        ("Rezept ändern", "orange", lambda: top_window(35)),
        ("Rezept löschen", "red", lambda: top_window(36)),
    ]

    meal_buttons = [
        ("Essen hinzufügen", "lightgreen", lambda: top_window(37)),
        ("Essen ändern", "orange", lambda: top_window(38)),
        ("Rezept anzeigen", "yellow", lambda: top_window(39)),
        ("Essen löschen", "red", lambda: top_window(40)),
        ("Woche 1 löschen", "red", lambda: top_window(41)),
        ("Woche 2 löschen", "red", lambda: top_window(42)),
    ]

    household_buttons = [
        ("Einnahme", "green", lambda: top_window(43)),
        ("Ausgabe", "red", lambda: top_window(44)),
        ("Holz", "brown", lambda: top_window(45)),
        ("Haushalt 4", "darkgrey", lambda: top_window(46)),
        ("Haushalt 5", "darkgrey", lambda: top_window(47)),
        ("Haushalt 6", "darkgrey", lambda: top_window(48)),
    ]

    return (
        config_buttons,
        view_buttons,
        todo_buttons,
        kids_buttons,
        calendar_buttons,
        shopping_buttons,
        recipes_buttons,
        meal_buttons,
        household_buttons,
    )


def overview():
    """Config Overview."""
    pass


def todo():
    """Config To-Do."""
    pass


def kids():
    """Config Kids."""
    pass


def calendar():
    """Config Calendar."""
    meetingBG = "yellow"
    meetingFG = "red"

    return meetingBG, meetingFG


def shop():
    """Config Recipe Treeview."""
    shop_one_width = 70
    shop_one_name = ""
    shop_one_sub = "Schnitzel"
    shop_one_values = ""
    shop_two_width = 70
    shop_two_name = ""
    shop_two_sub = "Paprika"
    shop_two_values = ""
    shop_three_width = 70
    shop_three_name = ""
    shop_three_sub = "Essen1"
    shop_three_values = ""

    shop_one = [shop_one_width, shop_one_name, shop_one_sub, shop_one_values]
    shop_two = [shop_two_width, shop_two_name, shop_two_sub, shop_two_values]
    shop_three = [shop_three_width, shop_three_name, shop_three_sub, shop_three_values]
    shop_categorie = ["Fleisch", "Gemüse", "Rezepte"]

    return (
        shop_one,
        shop_two,
        shop_three,
        shop_categorie,
    )


def recipe():
    """Config Recipe Treeview."""
    rec_one_width = 70
    rec_one_name = "Zeit"
    rec_one_sub = "Nudelsuppe"
    rec_one_values = "10", "Brühe"
    rec_two_width = 70
    rec_two_name = "Zutaten"
    rec_two_sub = "Nudeln mit Ei"
    rec_two_values = "5", "Ei"

    rec_one = [rec_one_width, rec_one_name, rec_one_sub, rec_one_values]
    rec_two = [rec_two_width, rec_two_name, rec_two_sub, rec_two_values]
    rec_categorie = ["Suppe", "Nudel"]

    return rec_one, rec_two, rec_categorie


def meal():
    """Config Meal."""
    week_day = [
        [
            ("Montag", 1),
            ("Dienstag", 2),
            ("Mittwoch", 3),
            ("Donnerstag", 4),
            ("Freitag", 5),
            ("Samstag", 6),
            ("Sonntag", 7),
        ],
        [
            ("Montag"),
            ("Dienstag"),
            ("Mittwoch"),
            ("Donnerstag"),
            ("Freitag"),
            ("Samstag"),
            ("Sonntag"),
        ],
    ]

    meal_week = [
        [
            ("Essen1", 1),
            ("Essen2", 2),
            ("Essen3", 3),
            ("Essen4", 4),
            ("Essen5", 5),
            ("Essen6", 6),
            ("Essen7", 7),
        ],
        [
            ("Essen8", 8),
            ("Essen9", 9),
            ("Essen10", 10),
            ("Essen11", 11),
            ("Essen12", 12),
            ("Essen13", 13),
            ("Essen14", 14),
        ],
    ]

    return week_day, meal_week


def home():
    """Config Home."""
    pass


sidebar_buttons = sidebar_buttons()
overview = overview()
todo = todo()
kids = kids()
calendar = calendar()
shop = shop()
recipe = recipe()
meal = meal()
home = home()
