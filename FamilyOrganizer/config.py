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
        "vertical.TNotebook",
        tabposition="w",
        tabmargins=0,
        padding=-5,
        background="lightgrey",
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
    cal_button1_text = "Termin anzeigen"
    cal_button2_text = "Termin suchen"
    cal_button3_text = "Termin ändern"
    cal_button4_text = "neuer Termin"
    cal_button5_text = "Termin löschen"
    cal_button6_text = "Terminübersicht"

    cal_colorbutton1 = "lightgrey"
    cal_colorbutton2 = "lightgrey"
    cal_colorbutton3 = "lightgrey"
    cal_colorbutton4 = "lightgreen"
    cal_colorbutton5 = "red"
    cal_colorbutton6 = "yellow"

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

    return week_day


overview = overview()
children = children()
calendar = calendar()
shopping = shopping()
recipe = recipe()
meal = meal()
