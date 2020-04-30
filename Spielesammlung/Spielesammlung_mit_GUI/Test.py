# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = Test.py
# __version__   =

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def show_choice(name, index, mode):
    """automatic update"""
    sf = "value is %s" % root.globalgetvar(name)
    # display update value in root window top frame
    root.title(sf)

def update_label():
    """update only after button click"""
    sf = "label2 text = %s" % stadt.get()
    label2["text"] = sf

root = tk.Tk()
root.title("Option Menu")

choices = ["Bochum", "Wilhelmshaven", "München", "Stuttgart"]

stadt = tk.StringVar(root)
# optionally preselect a choice (element 2)
stadt.set(choices[2])

stadt_option = tk.OptionMenu(root, stadt, *choices)
stadt_option.pack(padx=70, pady=20)

# one way to update selected option choice
stadt.trace('w', show_choice)

# another way textvariable --> automatic update of label text
label = tk.Label(root, textvariable=stadt)
label.pack()

# one more way, needs button click to update stadt choice
button = tk.Button(root, text="Update Label below", command=update_label)
label2 = tk.Label(root, text="--------")
button.pack(pady=20)
label2.pack()

root.mainloop()

# main = tk.Tk()
#
# lbBild = tk.Label(main)
# bild = tk.PhotoImage(file="arrow-green.png")
# lbBild["image_choice"] = bild
# lbBild.pack()

# a = {}
# print(a)
# test = "1"
# te = "a"
# add = {test:te}
# a.update(add)
# print(a)

# from tkinter import *
#
# cnt = 0
#
#
# def MsgClick(event):
#     children = root.winfo_children()
#     for child in children:
#         # print("type of widget is : " + str(type(child)))
#         if str(type(child)) == "<class 'tkinter.Message'>":
#             # print("Here Message widget will destroy")
#             child.destroy()
#             return
#
# def MsgMotion(event):
#   print("Mouse position: (%s %s)" % (event.x, event.y))
#   return
#
#
# def ButtonClick(event):
#     global cnt, msg
#     cnt += 1
#     msg = Message(root, text="you just clicked the button..." + str(cnt) + "...time...")
#     msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#     msg.bind("<Button-1>", MsgClick)
#     msg.bind("<Motion>", MsgMotion)
#     msg.pack()
#     #print(type(msg)) tkinter.Message
#
#
# def ButtonDoubleClick(event):
#     import sys; sys.exit()
#
#
# root = tk.Tk()
# main.title("Spielesammlung")                            # Fenstername
# main.configure(bg = "white")                            # Hintergrundfarbe
# main.minsize(width=400, height=400)                     # min. Fenstergröße
# main.maxsize(width=400, height=400)                     # max. Fenstergröße
# main.columnconfigure(0, weight = 3)                     # Zentrieren

# root.title("My First GUI App in Python")
# root.minsize(width=300, height=300)
# root.maxsize(width=400, height=350)
# button = Button(root, text="Click Me!", width=40, height=3)
# button.pack()
# button.bind("<Button-1>", ButtonClick)
# button.bind("<Double-1>", ButtonDoubleClick)
#
# root.mainloop()
# from PIL import Image, ImageTk
#
# def imgShow():
#     load = Image.open(pic[0])
#     render = ImageTk.PhotoImage(load)
#
#     img = Label(main, image_choice=render)
#     img.image_choice = render
#     img.place(x=0, y=0)
#
# pic = ["arrow-green.gif", "arrow-red.gif"]
#
# imgShow()
#
# main.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# height = 5
# width = 5
# for i in range(height): #Rows
#     for j in range(width): #Columns
#         b = Entry(root, text="")
#         b.grid(row=i, column=j)
#
# mainloop()
#
# guess = 2222
# hint_list = [[1, 1111, "aaaa"],[2, 2222, "bbbb"]]
# for tried in hint_list:
#     if tried[1] == guess:
#         print ("Found it!", tried[2])
#         break
# print(hint_list)

# import tensorflow as tf #Hier importieren wir die Library Tensorflow, welche für neuronale Netze der perfekte Einstieg ist. Eine Library ist ein vorgeschriebenes Programm. Es macht uns die Arbeit deutlich leichter
# from tensorflow import keras #hier importieren wir dann noch einen speziellen Teil aus Tensorflow. Keras. Hierzu später mehr.
#
# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) #hier definieren wir unser neuroanles Netz, wobei wir mit Dense unser Neuron erstellen. In diesem Beispiel nur eins, wir werden aber später sehen, dass man in der Regel mit deutlich mehr Neuronen arbeitet. Unser Neuron befindet sich in einem Layer, davon hat man später auch mehrere. Man kann sich dies wie Ebenen in einem Sieb vorstellen.
#
# model.compile(optimizer='sgd', loss='mean_squared_error') #hier kompilieren wir unser neuronales Netz, wobei der loss misst, wie groß der Fehler ist und dies dann mit optimizer optimiert wird
#
#
# xs=[1, 2, 3] #Zahlenreihe 1
# ys=[2, 4, 6] #Zahlenreihe 2
#
# model.fit(xs, ys, epochs=2000) #unser kompiliertes Modell fitten wir hier mit unseren zwei Zahlenreihen. epochs=1000 heißt, dass das Programm 1000 Durchläufer macht, um zu trainieren. Probiert gerne mal mit der Anzahl rum. Je weniger Durchläufe, desto schlechter ist die Schätzung. Gleichzeitig seht ihr, dass die Änderung im Loss immer weniger wird, je mehr Durchläufe es sind (es ist also irgendwann kaum noch eine Verbesserung sichtbar)
#
# print(model.predict([12])) #hier lassen wir unser neuronales Netz schätzen, was für die zweiten Zahl rauskommt, wenn die erste Zahl gleich 10 ist. Der Befehlt print sorgt hier einfach dafür, dass der Wert für uns ausgegeben wird.

# import tkinter as tk
# from tkinter import messagebox
# top = tk.Tk()
# top.title("Spielesammlung")                                                                # Fenstername
# top.configure(bg = "green")                                                                     # Hintergrundfarbe
# top.minsize(width=400, height=320)                                                         # min. Fenstergröße
# top.maxsize(width=400, height=320)                                                         # max. Fenstergröße
# top.columnconfigure(0, weight = 3)                                                         # Zentrieren
#
# photo = tk.PhotoImage(file = "table.png")
# w = tk.Label(top, image=photo)
# w.pack()
# ent = tk.Entry(w)
# ent.grid(column=0, row=0)
# ent2 = tk.Entry(w)
# ent2.grid(column=1, row=1)
# # ent.focus_set()
# top.mainloop()