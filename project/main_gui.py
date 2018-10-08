from tkinter import *
import send_mail
top = Tk()
top.geometry("100x100")
def send_mail_button():
    send_mail.main()

B = Button(top, text = "send_mail", command = send_mail_button)
B.place(x = 50,y = 50)

L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()
