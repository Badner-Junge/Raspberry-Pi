"""FamiliyOrganizer Modules.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from config import *
import os, config, tkinter.messagebox
import tkinter as tk


def fullscreen_toggle(self):
    """Fullscreen from menu.py."""
    menu.options.fullscreen_toggle(self)


def end(self):
    """Close Main Window."""
    root.destroy()
