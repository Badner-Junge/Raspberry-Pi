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
    """Tabs Position."""
    tabStyle = ttk.Style()
    tabStyle.configure("TNotebook", tabposition="w")


def Calendar(self):
    back = "red"
