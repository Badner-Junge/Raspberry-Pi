"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from modules import *
import modules, tkinter.messagebox
import tkinter as tk

# Aussehen
def style():
    """Config Style Tabs."""
    tabConfiguration = ttk.Style()
    tabConfiguration.configure(
        "main.TNotebook",
        tabposition="w",
        tabmargins=0,
        padding=-5,
        background="lightgrey",
    )
    tabConfiguration.configure(
        "kids.TNotebook",
        tabposition="n",
        tabmargins=0,
        padding=-5,
        background="lightgrey",
        fill="both",
        expand=True,
    )
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook.Tab", font="Comic 24", background="white")

    """Config Style Recipes."""
    treeStyle = ttk.Style()
    treeStyle.configure("Treeview", rowheight=50, font="Times 18")


# Übersicht
def overview():
    """Config Overview."""
    pass


# To-Do
def todo():
    """Config To-Do."""
    pass


# Kinder
def children():
    """Config Children."""
    pass


# Kalender
def calendar():
    """Config Calendar."""
    meetingBG = "yellow"
    meetingFG = "red"

    """Config Calendar Buttons."""
    cal_button1_text = "Terminübersicht"
    cal_button2_text = "Termin anzeigen"
    cal_button3_text = "Termin suchen"
    cal_button4_text = "Termin ändern"
    cal_button5_text = "neuer Termin"
    cal_button6_text = "Termin löschen"

    cal_colorbutton1 = "yellow"
    cal_colorbutton2 = "lightgrey"
    cal_colorbutton3 = "lightgrey"
    cal_colorbutton4 = "lightgrey"
    cal_colorbutton5 = "lightgreen"
    cal_colorbutton6 = "red"

    cal_button_text = [
        cal_button1_text,
        cal_button2_text,
        cal_button3_text,
        cal_button4_text,
        cal_button5_text,
        cal_button6_text,
    ]
    cal_button_color = [
        cal_colorbutton1,
        cal_colorbutton2,
        cal_colorbutton3,
        cal_colorbutton4,
        cal_colorbutton5,
        cal_colorbutton6,
    ]

    return meetingBG, meetingFG, cal_button_text, cal_button_color


# Einfaufen
def shopping():
    """Config Shopping."""
    pass


# Rezepte
def recipe():
    """Config Treeview."""
    one_width = 70
    one_name = "Zeit"
    one_sub = "Nudelsuppe"
    one_values = "10", "Brühe"
    two_width = 70
    two_name = "Zutaten"
    two_sub = "Nudeln mit Ei"
    two_values = "5", "Ei"

    one = [one_width, one_name, one_sub, one_values]
    two = [two_width, two_name, two_sub, two_values]
    categorie = ["Suppe", "Nudel"]

    """Config Recipe Buttons."""
    tree_button1_text = "Rezept anzeigen"
    tree_button2_text = "zum Essensplan"
    tree_button3_text = "neue Kategorie"
    tree_button4_text = "neues Rezept"
    tree_button5_text = "Rezept ändern"
    tree_button6_text = "Rezept löschen"

    tree_colorbutton1 = "lightgrey"
    tree_colorbutton2 = "lightgrey"
    tree_colorbutton3 = "lightgrey"
    tree_colorbutton4 = "lightgrey"
    tree_colorbutton5 = "lightgrey"
    tree_colorbutton6 = "red"

    tree_button_text = [
        tree_button1_text,
        tree_button2_text,
        tree_button3_text,
        tree_button4_text,
        tree_button5_text,
        tree_button6_text,
    ]
    tree_button_color = [
        tree_colorbutton1,
        tree_colorbutton2,
        tree_colorbutton3,
        tree_colorbutton4,
        tree_colorbutton5,
        tree_colorbutton6,
    ]

    return one, two, categorie, tree_button_text, tree_button_color


# Essensplan
def meal():
    """Config Meal."""
    week_day = [
        ("Montag", 1),
        ("Dienstag", 2),
        ("Mittwoch", 3),
        ("Donnerstag", 4),
        ("Freitag", 5),
        ("Samstag", 6),
        ("Sonntag", 7),
    ]

    day = [
        ("Montag"),
        ("Dienstag"),
        ("Mittwoch"),
        ("Donnerstag"),
        ("Freitag"),
        ("Samstag"),
        ("Sonntag"),
    ]

    """Config Meal Buttons."""
    meal_button1_text = "Essen hinzufügen"
    meal_button2_text = "Essen ändern"
    meal_button3_text = "?"
    meal_button4_text = "Essen löschen"
    meal_button5_text = "Woche 1 löschen"
    meal_button6_text = "Woche 2 löschen"

    meal_colorbutton1 = "lightgrey"
    meal_colorbutton2 = "lightgrey"
    meal_colorbutton3 = "lightgrey"
    meal_colorbutton4 = "red"
    meal_colorbutton5 = "red"
    meal_colorbutton6 = "red"

    meal_button_text = [
        meal_button1_text,
        meal_button2_text,
        meal_button3_text,
        meal_button4_text,
        meal_button5_text,
        meal_button6_text,
    ]
    meal_button_color = [
        meal_colorbutton1,
        meal_colorbutton2,
        meal_colorbutton3,
        meal_colorbutton4,
        meal_colorbutton5,
        meal_colorbutton6,
    ]

    return week_day, day, meal_button_text, meal_button_color


# Haushalt
def home():
    """Config Home."""
    pass


overview = overview()
todo = todo()
children = children()
calendar = calendar()
shopping = shopping()
recipe = recipe()
meal = meal()
home = home()
