from tkinter import *
from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue")
filename = PhotoImage(file = "accident1.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
e = Entry(top,width=100)
e.pack()

C.pack()
top.mainloop()
