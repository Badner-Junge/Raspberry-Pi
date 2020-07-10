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

    """Config Spinbox."""
    spinStyle = ttk.Style()
    spinStyle.configure("TSpinbox", arrowsize=35)


def sidebar_buttons():
    """Config Sidebar Buttonname, Buttoncolor, Toplevel."""
    config_buttons = [14, "Times 12 bold"]  # width  # font, size

    # Übersicht
    view_buttons = [
        ("view1", "grey", lambda: top_window(1)),
        ("view2", "grey", lambda: top_window(2)),
        ("view3", "grey", lambda: top_window(3)),
        ("view4", "grey", lambda: top_window(4)),
        ("view5", "grey", lambda: top_window(5)),
        ("view6", "grey", lambda: top_window(6)),
    ]

    # To-Do
    todo_buttons = [
        ("Katja", "green", lambda: top_window(7)),
        ("Fabian", "green", lambda: top_window(8)),
        ("Fabienne", "red", lambda: top_window(9)),
        ("Mio", "orange", lambda: top_window(10)),
        ("Mika", "yellow", lambda: top_window(11)),
        ("Jona", "beige", lambda: top_window(12)),
    ]

    # Kinder
    kids_buttons = [
        ("Kinder 1", "purple", lambda: top_window(13)),
        ("Kinder 2", "white", lambda: top_window(14)),
        ("Kinder 3", "green", lambda: top_window(15)),
        ("Kinder 4", "orange", lambda: top_window(16)),
        ("Kinder 5", "pink", lambda: top_window(17)),
        ("Kinder 6", "brown", lambda: top_window(18)),
    ]

    # Kalender
    calendar_buttons = [
        ("Terminübersicht", "yellow", lambda: top_window(19)),
        ("Termin anzeigen", "yellow", lambda: top_window(20)),
        ("Termin suchen", "yellow", lambda: top_window(21)),
        ("Termin ändern", "orange", lambda: top_window(22)),
        ("neuer Termin", "lightgreen", lambda: top_window(23)),
        ("Termin löschen", "red", lambda: top_window(24)),
    ]

    # Einkaufen
    shopping_buttons = [
        ("neue Kategorie\nneuer Artikel", "lightgreen", lambda: top_window(25)),
        ("Artikel\neinkaufen", "lightgreen", lambda: top_window(26)),
        ("Artikel\nMenge ändern", "orange", lambda: top_window(27)),
        ("Artikel aus Liste\nlöschen", "red", lambda: top_window(28)),
        ("ganze Liste\n löschen", "red", lambda: top_window(29)),
        ("Drucken", "blue", lambda: top_window(30)),
    ]

    # Rezepte
    recipes_buttons = [
        ("Rezept anzeigen", "yellow", lambda: top_window(31)),
        ("zum Essensplan", "lightgreen", lambda: top_window(32)),
        ("neue Kategorie", "lightgreen", lambda: top_window(33)),
        ("neues Rezept", "lightgreen", lambda: top_window(34)),
        ("Rezept ändern", "orange", lambda: top_window(35)),
        ("Rezept löschen", "red", lambda: top_window(36)),
    ]

    # Essensplan
    meal_buttons = [
        ("Essen hinzufügen", "lightgreen", lambda: top_window(37)),
        ("Essen ändern", "orange", lambda: top_window(38)),
        ("Rezept anzeigen", "yellow", lambda: top_window(39)),
        ("Essen löschen", "red", lambda: top_window(40)),
        ("Woche 1 löschen", "red", lambda: top_window(41)),
        ("Woche 2 löschen", "red", lambda: top_window(42)),
    ]

    # Haushaltsbuch
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
    con = sqlite3.connect("family_data.db")
    cursor = con.cursor()
    id_shop = "SELECT id_shop_cat FROM shop_cat"
    cursor.execute(id_shop)
    id_shop_list = []
    for id_cat in cursor:
        id_shop_list.append(id_cat)
    cursor.close()

    cursor = con.cursor()
    name_shop = "SELECT name_shop_cat FROM shop_cat"
    cursor.execute(name_shop)
    name_shop_list = []
    for name in cursor:
        name_shop_list.append(name)
    cursor.close()

    cursor = con.cursor()
    dir_shop = "SELECT dir FROM shop_cat"
    cursor.execute(dir_shop)
    dir_shop_list = []
    for Dir in cursor:
        dir_shop_list.append(Dir)
    cursor.close()

    cursor = con.cursor()
    sub1_shop = "SELECT sub1 FROM shop_cat"
    cursor.execute(sub1_shop)
    sub1_shop_list = []
    for sub1 in cursor:
        sub1_shop_list.append(sub1)
    cursor.close()

    cursor = con.cursor()
    sub2_shop = "SELECT sub2 FROM shop_cat"
    cursor.execute(sub2_shop)
    sub2_shop_list = []
    for sub2 in cursor:
        sub2_shop_list.append(sub2)
    cursor.close()

    cursor = con.cursor()
    sub3_shop = "SELECT sub3 FROM shop_cat"
    cursor.execute(sub3_shop)
    sub3_shop_list = []
    for sub3 in cursor:
        sub3_shop_list.append(sub3)
    cursor.close()

    cursor = con.cursor()
    main_shop = "SELECT main FROM shop_cat"
    cursor.execute(main_shop)
    main_shop_list = []
    for main in cursor:
        main_shop_list.append(main)
    cursor.close()

    cursor = con.cursor()
    id_shop_item = "SELECT id_shop_item FROM shop_items"
    cursor.execute(id_shop_item)
    id_shop_item_list = []
    for item in cursor:
        id_shop_item_list.append(item)
    cursor.close()

    cursor = con.cursor()
    name_shop_item = "SELECT item_name FROM shop_items"
    cursor.execute(name_shop_item)
    name_shop_item_list = []
    for name in cursor:
        name_shop_item_list.append(name)
    cursor.close()

    cursor = con.cursor()
    size_shop_item = "SELECT item_size FROM shop_items"
    cursor.execute(size_shop_item)
    size_shop_item_list = []
    for size in cursor:
        size_shop_item_list.append(size)
    cursor.close()

    cursor = con.cursor()
    measurement_shop_item = "SELECT item_measurement FROM shop_items"
    cursor.execute(measurement_shop_item)
    measurement_shop_item_list = []
    for measurement in cursor:
        measurement_shop_item_list.append(measurement)
    cursor.close()

    cursor = con.cursor()
    dir_shop_item = "SELECT item_dir FROM shop_items"
    cursor.execute(dir_shop_item)
    dir_shop_item_list = []
    for dir_item in cursor:
        dir_shop_item_list.append(dir_item)
    cursor.close()

    cursor = con.cursor()
    main_shop_item = "SELECT item_main FROM shop_items"
    cursor.execute(main_shop_item)
    main_shop_item_list = []
    for main_item in cursor:
        main_shop_item_list.append(main_item)
    cursor.close()

    measurementList = ["ml", "l", "g", "kg", "Stück"]

    cursor = con.cursor()
    buy_shop_item = "SELECT item_buy FROM shop_items"
    cursor.execute(buy_shop_item)
    buy_shop_item_list = []
    for buy_item in cursor:
        buy_shop_item_list.append(buy_item)
    cursor.close()

    cursor = con.cursor()
    pieces_shop_item = "SELECT item_pieces FROM shop_items"
    cursor.execute(pieces_shop_item)
    pieces_shop_item_list = []
    for pieces_item in cursor:
        pieces_shop_item_list.append(pieces_item)
    cursor.close()

    return (
        id_shop_list,  # 0
        name_shop_list,  # 1
        dir_shop_list,  # 2
        sub1_shop_list,  # 3
        sub2_shop_list,  # 4
        sub3_shop_list,  # 5
        main_shop_list,  # 6
        id_shop_item_list,  # 7
        name_shop_item_list,  # 8
        size_shop_item_list,  # 9
        measurement_shop_item_list,  # 10
        dir_shop_item_list,  # 11
        main_shop_item_list,  # 12
        measurementList,  # 13
        buy_shop_item_list,  # 14
        pieces_shop_item_list,  # 15
    )


def recipe():
    """Config (rec_conf) Treeview."""
    con = sqlite3.connect("family_data.db")
    cursor = con.cursor()
    id_conf = "SELECT id_config FROM rec_conf"
    cursor.execute(id_conf)
    id_config = []
    for conf in cursor:
        id_config.append(conf)
    cursor.close()

    cursor = con.cursor()
    col = "SELECT columns FROM rec_conf"
    cursor.execute(col)
    rec_columns = []
    for column in cursor:
        rec_columns.append(column)
    cursor.close()

    cursor = con.cursor()
    head = "SELECT heading FROM rec_conf"
    cursor.execute(head)
    rec_heading = []
    for heading in cursor:
        rec_heading.append(heading)
    cursor.close()

    cursor = con.cursor()
    width = "SELECT width FROM rec_conf"
    cursor.execute(width)
    rec_column_width = []
    for number in cursor:
        rec_column_width.append(number)
    cursor.close()

    """Config (rec_cat) Treeview."""
    cursor = con.cursor()
    id_cat = "SELECT id_categorie FROM rec_cat"
    cursor.execute(id_cat)
    id_categorie = []
    for cat in cursor:
        id_categorie.append(cat)
    cursor.close()

    cursor = con.cursor()
    categ = "SELECT categorie FROM rec_cat"
    cursor.execute(categ)
    rec_categorie = []
    for cat in cursor:
        rec_categorie.append(cat)
    cursor.close()

    cursor = con.cursor()
    cat_dir = "SELECT dir FROM rec_cat"
    cursor.execute(cat_dir)
    rec_categorie_dir = []
    for Dir in cursor:
        rec_categorie_dir.append(Dir)
    cursor.close()

    cursor = con.cursor()
    cat_sub1 = "SELECT sub1 FROM rec_cat"
    cursor.execute(cat_sub1)
    rec_categorie_sub1 = []
    for sub1 in cursor:
        rec_categorie_sub1.append(sub1)
    cursor.close()

    cursor = con.cursor()
    cat_sub2 = "SELECT sub2 FROM rec_cat"
    cursor.execute(cat_sub2)
    rec_categorie_sub2 = []
    for sub2 in cursor:
        rec_categorie_sub2.append(sub2)
    cursor.close()

    """Config (rec_recipe) Treeview."""
    cursor = con.cursor()
    id_rec = "SELECT id_recipe FROM rec_recipe"
    cursor.execute(id_rec)
    id_recipe = []
    for recip in cursor:
        id_recipe.append(recip)
    cursor.close()

    cursor = con.cursor()
    nam_cat = "SELECT rec_categorie FROM rec_recipe"
    cursor.execute(nam_cat)
    rec_name_cat = []
    for name_cat in cursor:
        rec_name_cat.append(name_cat)
    cursor.close()

    cursor = con.cursor()
    nam = "SELECT name FROM rec_recipe"
    cursor.execute(nam)
    rec_name = []
    for name in cursor:
        rec_name.append(name)
    cursor.close()

    cursor = con.cursor()
    rec = "SELECT recipe FROM rec_recipe"
    cursor.execute(rec)
    rec_recipe = []
    for recipe in cursor:
        rec_recipe.append(recipe)
    cursor.close()

    cursor = con.cursor()
    ingr = "SELECT ingredient FROM rec_recipe"
    cursor.execute(ingr)
    rec_ingredient = []
    for ingredient in cursor:
        rec_ingredient.append(ingredient)
    cursor.close()

    cursor = con.cursor()
    meas = "SELECT measurement FROM rec_recipe"
    cursor.execute(meas)
    rec_measurement = []
    for measurement in cursor:
        rec_measurement.append(measurement)
    cursor.close()

    timeList = ["schnell", "mittel", "lang"]

    # categorieList = rec_categorie

    cursor = con.cursor()
    week1 = "SELECT week1 FROM rec_recipe"
    cursor.execute(week1)
    week1_list = []
    for week1_day in cursor:
        week1_list.append(week1_day)
    cursor.close()

    cursor = con.cursor()
    week2 = "SELECT week2 FROM rec_recipe"
    cursor.execute(week2)
    week2_list = []
    for week2_day in cursor:
        week2_list.append(week2_day)
    cursor.close()
    con.close()

    return (
        id_config,  # 0
        rec_columns,  # 1
        rec_heading,  # 2
        rec_column_width,  # 3
        id_categorie,  # 4
        rec_categorie,  # 5
        rec_categorie_dir,  # 6
        rec_categorie_sub1,  # 7
        rec_categorie_sub2,  # 8
        id_recipe,  # 9
        rec_name_cat,  # 10
        rec_name,  # 11
        rec_recipe,  # 12
        rec_ingredient,  # 13
        rec_measurement,  # 14
        timeList,  # 15
        week1_list,  # 16
        week2_list  # 17
        # categorieList,  # 16
    )


def meal():
    """Config Meal."""
    con = sqlite3.connect("family_data.db")
    cursor = con.cursor()
    id_meal = "SELECT id_day FROM meal_days"
    cursor.execute(id_meal)
    id_meal_list = []
    for id_day in cursor:
        id_meal_list.append(id_day)
    cursor.close()

    cursor = con.cursor()
    day_meal = "SELECT day FROM meal_days"
    cursor.execute(day_meal)
    day_meal_list = []
    for day_day in cursor:
        day_meal_list.append(day_day)
    cursor.close()

    return id_meal_list, day_meal_list


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
