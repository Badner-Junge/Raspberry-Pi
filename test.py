from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import os

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


# class Root(Tk):
#     def __init__(self):
#         super(Root, self).__init__()
#         self.title("Application")
#         self.minsize(640, 400)
#         self.configure(background="white")

#         self.createMenu()

#         tabControl = ttk.Notebook(self)
#         self.tab1 = ttk.Frame(tabControl)
#         tabControl.add(self.tab1, text="tab 1")

#         self.tab2 = ttk.Frame(tabControl)
#         tabControl.add(self.tab2, text="tab 2")

#         self.tab3 = ttk.Frame(tabControl)
#         tabControl.add(self.tab3, text="tab 3")

#         self.tab4 = ttk.Frame(tabControl)
#         tabControl.add(self.tab4, text="tab 4")
#         self.addingTab4()

#         self.tab5 = ttk.Frame(tabControl)
#         tabControl.add(self.tab5, text="tab 5")

#         self.tab6 = ttk.Frame(tabControl)
#         tabControl.add(self.tab6, text="tab 6")

#         self.tab7 = ttk.Frame(tabControl)
#         tabControl.add(self.tab7, text="Tab 7")

#         tabControl.pack(expand=1, fill="both")

#         self.tab_control = tabControl

#     def startpressed(self):
#         new = tk.Toplevel(self)
#         new.minsize(640, 400)
#         new.geometry("500x300")
#         new.configure(background="white")
#         tabControl1 = ttk.Notebook(new)
#         new.tab1 = ttk.Frame(tabControl1)
#         tabControl1.add(new.tab1, text="tab 1")
#         tabControl1.pack(expand=1, fill="both")

#     def createMenu(self):
#         menubar = Menu(self)
#         self.config(menu=menubar)

#         file_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="File", menu=file_menu)
#         file_menu.add_command(label="Exit")

#         help_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Help", menu=help_menu)
#         help_menu.add_command(label="About Us")

#     def addingTab4(self):
#         Label(self.tab4, text="Please Select your choice").place(x=250, y=20)
#         submit = Button(self.tab4, text="Submit", command=lambda: self.submit()).place(
#             x=520, y=320
#         )

#     def submit(self):
#         newTop = Toplevel(self.master)
#         display = Label(newTop, text="Review").pack()
#         newTop.title("Review and Submit")
#         newTop.focus_set()
#         newTop.geometry("400x600")
#         # WOULD LIKE: when this button is clicked it takes the user to tab 7 of the notebook window
#         btnResult = Button(newTop, text="Tab 7", command=self.result1).pack()
#         btnBack = Button(newTop, text="Back").pack()

#     def result1(self):
#         # ttk.Notebook.select(self.tab7)
#         self.tab_control.select(self.tab7)


# root = Root()
# root.mainloop()


""" Kalender."""
# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import *
# import tkcalendar
# from tkcalendar import Calendar, DateEntry
# import datetime

# root = tk.Tk()

# events = {
#     "2018-09-28": ("London", "meeting"),
#     "2018-08-15": ("Paris", "meeting"),
#     "2018-07-30": ("New York", "meeting"),
# }

# cal = Calendar(root, selectmode="day", year=2018, month=8)

# for k in events.keys():
#     date = datetime.datetime.strptime(k, "%Y-%m-%d").date()
#     cal.calevent_create(date, events[k][0], events[k][1])

# cal.tag_config("meeting", background="red", foreground="yellow")
# cal.pack(fill="both", expand=True)

# root.mainloop()

# try:
#     # Python2
#     import Tkinter as tk
#     import ttk
# except ImportError:
#     # Python3
#     import tkinter as tk
#     import tkinter.ttk as ttk

# root = tk.Tk()
# # use width x height + x_offset + y_offset (no spaces!)
# root.geometry("%dx%d+%d+%d" % (300, 200, 100, 50))
# root.title("testing the ttk.Notebook")

# nb = ttk.Notebook(root)
# nb.pack(fill="both", expand="yes")

# # create a child frame for each page
# f1 = tk.Frame(bg="red")
# f2 = tk.Frame(bg="blue")
# f3 = tk.Frame(bg="green")

# # create the pages, text goes on the tabs
# nb.add(f1, text="page1")
# nb.add(f2, text="page2")
# nb.add(f3, text="page3")

# # put a button widget on child frame f1 on page1
# button1 = tk.Button(f1, text="button1")
# button1.pack(side="left", anchor="nw", padx=3, pady=5)

# # put a combo box widget on child frame f2 on page2
# combo = ttk.Combobox(f2)
# shop_list = ["grapes", "pears", "onions"]
# combo["values"] = shop_list
# combo.set(shop_list[0])
# combo.pack(side="left", anchor="nw", padx=3, pady=5)

# # put something different into frame f3 on page3
# listbox = tk.Listbox(f3, bg="yellow")
# for item in shop_list:
#     listbox.insert("end", item)
# listbox.pack(side="left", anchor="nw", padx=3, pady=5)

# root.mainloop()


root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)]


def ShowChoice():
    print(v.get())


Label(
    root,
    text="""Choose your favourite 
programming language:""",
    justify=LEFT,
    padx=20,
).pack()

for txt, val in languages:
    Radiobutton(
        root,
        text=txt,
        indicatoron=0,
        width=20,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
    ).pack(anchor=W)
mainloop()
