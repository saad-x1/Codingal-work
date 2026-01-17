from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greeting = Label(text="Hello User", fg='black', bg='white')
button = Button(text="Click me", bg='black', fg='white')
entry = Entry(fg='yellow', bg='blue', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text='Sample Frame')
label.pack()
window.mainloop()

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()

