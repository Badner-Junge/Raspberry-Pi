"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from test_modules import *
import test_modules, tkinter.messagebox
import tkinter as tk

# Aussehen
def style():
    """Config Style."""

    # Notebook Tab Position
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

    # Notebook Tab Style
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook.Tab", font="Comic 24", background="white")

    # Treeview
    treeStyle = ttk.Style()
    treeStyle.configure("recipes.Treeview", rowheight=50, font="Times 18")

    # Buttons
    treeStyle = ttk.Style()
    treeStyle.configure("TButtons")


# Sidebar Knöpfe
def sidebar_config():

    todo_buttons = [
        ("Katja", "green"),
        ("Fabian", "green"),
        ("Fabienne", "red"),
        ("Mio", "orange"),
        ("Mika", "yellow"),
        ("Jona", "beige"),
    ]

    return todo_buttons


# Übersicht
def view_config():
    """Config Overview."""
    pass


# To-Do
def todo_config():
    """Config To-Do Buttons."""
    todo_button1_text = "Katja"
    todo_button2_text = "Fabian"
    todo_button3_text = "Fabienne"
    todo_button4_text = "Mio"
    todo_button5_text = "Mika"
    todo_button6_text = "Jona"

    todo_colorbutton1 = "green"
    todo_colorbutton2 = "green"
    todo_colorbutton3 = "red"
    todo_colorbutton4 = "orange"
    todo_colorbutton5 = "yellow"
    todo_colorbutton6 = "beige"

    todo_button_text = [
        todo_button1_text,
        todo_button2_text,
        todo_button3_text,
        todo_button4_text,
        todo_button5_text,
        todo_button6_text,
    ]
    todo_button_color = [
        todo_colorbutton1,
        todo_colorbutton2,
        todo_colorbutton3,
        todo_colorbutton4,
        todo_colorbutton5,
        todo_colorbutton6,
    ]

    return todo_button_text, todo_button_color


# Kinder
def kids_config():
    """Config Kids Buttons."""
    kids_button1_text = "Kinder 1"
    kids_button2_text = "Kinder 2"
    kids_button3_text = "Kinder 3"
    kids_button4_text = "Kinder 4"
    kids_button5_text = "Kinder 5"
    kids_button6_text = "Kinder 6"

    kids_colorbutton1 = "purple"
    kids_colorbutton2 = "white"
    kids_colorbutton3 = "green"
    kids_colorbutton4 = "orange"
    kids_colorbutton5 = "pink"
    kids_colorbutton6 = "brown"

    kids_button_text = [
        kids_button1_text,
        kids_button2_text,
        kids_button3_text,
        kids_button4_text,
        kids_button5_text,
        kids_button6_text,
    ]
    kids_button_color = [
        kids_colorbutton1,
        kids_colorbutton2,
        kids_colorbutton3,
        kids_colorbutton4,
        kids_colorbutton5,
        kids_colorbutton6,
    ]

    return kids_button_text, kids_button_color


# Kalender
def calendar_config():
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
    cal_colorbutton2 = "yellow"
    cal_colorbutton3 = "yellow"
    cal_colorbutton4 = "orange"
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
def shop_config():
    """Config Recipe Treeview."""
    buy_one_width = 70
    buy_one_name = ""
    buy_one_sub = "Schnitzel"
    buy_one_values = ""
    buy_two_width = 70
    buy_two_name = ""
    buy_two_sub = "Paprika"
    buy_two_values = ""
    buy_three_width = 70
    buy_three_name = ""
    buy_three_sub = "Essen1"
    buy_three_values = ""

    buy_one = [buy_one_width, buy_one_name, buy_one_sub, buy_one_values]
    buy_two = [buy_two_width, buy_two_name, buy_two_sub, buy_two_values]
    buy_three = [buy_three_width, buy_three_name, buy_three_sub, buy_three_values]
    buy_categorie = ["Fleisch", "Gemüse", "Rezepte"]

    """Config Buy Buttons."""
    buy_button1_text = "Artikel hinzufügen"
    buy_button2_text = "Rezept hinzufügen"
    buy_button3_text = "Menge ändern"
    buy_button4_text = "Artikel löschen"
    buy_button5_text = "Liste löschen"
    buy_button6_text = "Drucken"

    buy_colorbutton1 = "lightgreen"
    buy_colorbutton2 = "lightgreen"
    buy_colorbutton3 = "orange"
    buy_colorbutton4 = "red"
    buy_colorbutton5 = "red"
    buy_colorbutton6 = "blue"

    buy_button_text = [
        buy_button1_text,
        buy_button2_text,
        buy_button3_text,
        buy_button4_text,
        buy_button5_text,
        buy_button6_text,
    ]
    buy_button_color = [
        buy_colorbutton1,
        buy_colorbutton2,
        buy_colorbutton3,
        buy_colorbutton4,
        buy_colorbutton5,
        buy_colorbutton6,
    ]

    return buy_one, buy_two, buy_categorie, buy_button_text, buy_button_color, buy_three


# Rezepte
def recipes_config():
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

    """Config Recipe Buttons."""
    rec_tree_button1_text = "Rezept anzeigen"
    rec_tree_button2_text = "zum Essensplan"
    rec_tree_button3_text = "neue Kategorie"
    rec_tree_button4_text = "neues Rezept"
    rec_tree_button5_text = "Rezept ändern"
    rec_tree_button6_text = "Rezept löschen"

    rec_tree_colorbutton1 = "yellow"
    rec_tree_colorbutton2 = "lightgreen"
    rec_tree_colorbutton3 = "lightgreen"
    rec_tree_colorbutton4 = "lightgreen"
    rec_tree_colorbutton5 = "orange"
    rec_tree_colorbutton6 = "red"

    rec_tree_button_text = [
        rec_tree_button1_text,
        rec_tree_button2_text,
        rec_tree_button3_text,
        rec_tree_button4_text,
        rec_tree_button5_text,
        rec_tree_button6_text,
    ]
    rec_tree_button_color = [
        rec_tree_colorbutton1,
        rec_tree_colorbutton2,
        rec_tree_colorbutton3,
        rec_tree_colorbutton4,
        rec_tree_colorbutton5,
        rec_tree_colorbutton6,
    ]

    return rec_one, rec_two, rec_categorie, rec_tree_button_text, rec_tree_button_color


# Essensplan
def meal_config():
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
    meal_button3_text = "Rezept anzeigen"
    meal_button4_text = "Essen löschen"
    meal_button5_text = "Woche 1 löschen"
    meal_button6_text = "Woche 2 löschen"

    meal_colorbutton1 = "lightgreen"
    meal_colorbutton2 = "orange"
    meal_colorbutton3 = "yellow"
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

    meal_week1 = [
        ("Essen1", 1),
        ("Essen2", 2),
        ("Essen3", 3),
        ("Essen4", 4),
        ("Essen5", 5),
        ("Essen6", 6),
        ("Essen7", 7),
    ]
    meal_week2 = [
        ("Essen8", 8),
        ("Essen9", 9),
        ("Essen10", 10),
        ("Essen11", 11),
        ("Essen12", 12),
        ("Essen13", 13),
        ("Essen14", 14),
    ]

    return week_day, day, meal_button_text, meal_button_color, meal_week1, meal_week2


# Haushalt
def house_config():
    """Config Home."""
    pass


sidebar_config = sidebar_config()
view_config = view_config()
todo_config = todo_config()
kids_config = kids_config()
calendar_config = calendar_config()
shop_config = shop_config()
recipes_config = recipes_config()
meal_config = meal_config()
house_config = house_config()
