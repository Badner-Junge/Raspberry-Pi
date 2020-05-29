"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
from tabs import *


# class Config:
#     """Style Settings."""


def Tabs(self):
    """Config Tabs."""
    tabConfiguration = ttk.Style()
    tabConfiguration.configure(
        "TNotebook", tabposition="w", tabmargins=0, padding=-5, background="grey"
    )
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook.Tab", font="Comic 24", background="white")


def Calendar(self):
    back = "red"
