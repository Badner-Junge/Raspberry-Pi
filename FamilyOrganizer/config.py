"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tabs import *
import tabs
import tkinter.messagebox
import tkinter as tk


def Style():
    """Config Tabs."""
    tabConfiguration = ttk.Style()
    tabConfiguration.configure(
        "TNotebook", tabposition="w", tabmargins=0, padding=-5, background="lightgrey"
    )
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook.Tab", font="Comic 24", background="white")

    treeStyle = ttk.Style()
    treeStyle.configure("Treeview", rowheight=50, font="Times 18")


def Calendar():
    """Config Calendar."""
    meetingBG = "yellow"
    meetingFG = "red"

    return meetingBG, meetingFG


def Tree():
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

    return one, two, categorie


def Recipe():

    recipe_bg = "lightgrey"
    recipe = ["Rezept"]

    return recipe, recipe_bg


calendar = Calendar()
tree = Tree()
recipe = Recipe()
