from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from data_access import data_retrive
from send_mail import sendmail
from HoverInfo import HoverInfo

import sqlite3 #this is DB package

conn = sqlite3.connect('accident.db')



# functions will be declared form here
class UserInfo:
    def __init__(self,master):

        # frames will be here
        frame1 = Frame(master,padx=30)
        frame1.pack(side=LEFT)

        frame2 = Frame(master,padx=200,bg="green")
        frame2.pack(fill=X)






        # creating the ten buttons and entry option
        self.e = ttk.Entry(frame1,width=100)
        self.e.pack(anchor=CENTER)

        help = ttk.Button(frame1,text="help",command=self.user)
        help.pack(pady=30)


        # for the user database

        insert_user = ttk.Button(frame2,text="  insert_user   ",command=self.insert_user)
        insert_user.pack(pady=30)



        update_user = ttk.Button(frame2,text="  update_user   ",command=self.update_user)
        update_user.pack(pady=30)



        delete_user = ttk.Button(frame2,text="  delete_user   ",command=self.delete_user)
        delete_user.pack(pady=30)




        # for the hospital database
        insert_hospital = ttk.Button(frame2,text="insert_hospital ",command=self.insert_hospital)
        insert_hospital.pack(pady=30)



        update_hospital = ttk.Button(frame2,text="update_hospital ",command=self.update_hospital)
        update_hospital.pack(pady=30)



        delete_hospital = ttk.Button(frame2,text="delete_hospital ",command=self.delete_hospital)
        delete_hospital.pack(pady=30)



        # for the policy database
        insert_policy = ttk.Button(frame2,text=" insert_policy ",command=self.insert_policy)
        insert_policy.pack(pady=30)



        update_policy = ttk.Button(frame2,text=" update_policy ",command=self.update_policy)
        update_policy.pack(pady=30)



        delete_policy = ttk.Button(frame2,text=" delete_policy ",command=self.delete_policy)
        delete_policy.pack(pady=30)

        # buttons decleration was done


    def user(self):
        userid = int(self.e.get())
        msg = data_retrive(userid)
        messagebox.showinfo("DataBase Snippet",msg)
        sendmail()
        messagebox.showinfo("mail sent acknowledgment","we done it! \n every mail over there are identified and accnowledgment was sent")


    def insert_user(self):
        c = Insert_User_Form()
        c.insert_user_fn()

    def update_user(self):
        c = Update_User_Form()
        c.update_user_fn()

    def delete_user(self):
        c = Delete_User_Form()
        c.delete_user_fn()

    def insert_hospital(self):
        c = Insert_Hospital_Form()
        c.insert_hospital_fn()

    def update_hospital(self):
        c = Update_Hospital_Form()
        c.update_hospital_fn()

    def delete_hospital(self):
        c = Delete_Hospital_Form()
        c.delete_hospital_fn()

    def insert_policy(self):
        c = Insert_Policy_Form()
        c.insert_policy_fn()

    def update_policy(self):
        c = Update_Policy_Form()
        c.update_policy_fn()

    def delete_policy(self):
        c = Delete_Policy_Form()
        c.delete_policy_fn()



"""
this is the class implementation
completely belonging to the user

insert
update
and
delete
OPERATIONS
in Tkinter GUI

"""
class Insert_User_Form():
    def __init__(self):
        new = Tk()
        new.title("Inserting An Element In the USER DataBase")
        label = ttk.Label(new,text="USERID ,USEREMAIL ,HOSPITALID ,POLICYID ,NAME ,AGE ,GENDER ,CITY\n Please enter the details of the user in this format")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        insert = ttk.Button(new,text="  insert_user   ",command=self.insert_user_fn)
        insert.pack()
        new.mainloop()


    def insert_user_fn(self):
        entry = self.e1.get()
        entry = entry.split()

        conn.execute("INSERT INTO USER VALUES (?, ?, ?, ?,?, ?, ?, ?);", (int(entry[0]),entry[1],int(entry[2]),int(entry[3]),entry[4],int(entry[5]),entry[6],entry[7]))
        conn.commit()

class Update_User_Form():
    def __init__(self):
        new = Tk()
        new.title("updating An Element In the USER DataBase")
        label = ttk.Label(new,text="These OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  update   ",command=self.update_user_fn)
        update.pack()
        new.mainloop()


    def update_user_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()

class Delete_User_Form():
    def __init__(self):
        new = Tk()
        new.title("Deleting An Element In the User DataBase")
        label = ttk.Label(new,text="These OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  Delete   ",command=self.delete_user_fn)
        update.pack()
        new.mainloop()


    def delete_user_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()





"""
this is the class implementation
completely belonging to the
Hospital DataBase

insert
update
and
delete
OPERATIONS
in Tkinter GUI

"""

class Insert_Hospital_Form():
    def __init__(self):
        new = Tk()
        new.title("Inserting An Element In the HOSPITAL DataBase")
        label = ttk.Label(new,text="New entry in Hospital Window\nHOSPITALID, HospitalEmail, HospitalName\n Please enter the details of the user in this format")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        insert = ttk.Button(new,text="  insert_user   ",command=self.insert_hospital_fn)
        insert.pack()
        new.mainloop()


    def insert_hospital_fn(self):
        entry = self.e1.get()
        entry = entry.split()
        uid = int(entry[0])

        conn.execute("INSERT INTO HOSPITAL VALUES (?, ?, ?);", (int(entry[0]),entry[1],entry[2]))
        conn.commit()

class Update_Hospital_Form():
    def __init__(self):
        new = Tk()
        new.title("updating An Element In the HOSPITAL DataBase")
        label = ttk.Label(new,text="Update Hospital Window\nThese OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  update   ",command=self.update_hospital_fn)
        update.pack()
        new.mainloop()


    def update_hospital_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()

class Delete_Hospital_Form():
    def __init__(self):
        new = Tk()
        new.title("Deleting An Element In the HOSPITAL DataBase")
        label = ttk.Label(new,text="Delete Hospital Window\nThese OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  Delete   ",command=self.delete_hospital_fn)
        update.pack()
        new.mainloop()


    def delete_hospital_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()





"""
this is the class implementation
completely belonging to the
policy DataBase

insert
update
and
delete
OPERATIONS
in Tkinter GUI

"""



class Insert_Policy_Form():
    def __init__(self):
        new = Tk()
        new.title("Inserting An Element In the POLICY DataBase")
        label = ttk.Label(new,text="Policy new Entry window\nPOLICYID, POLICYEMAIL, POLICYNAME\n Please enter the details of the user in this format")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        insert = ttk.Button(new,text="  insert_user   ",command=self.insert_policy_fn)
        insert.pack()
        new.mainloop()


    def insert_policy_fn(self):
        entry = self.e1.get()
        entry = entry.split()

        conn.execute("INSERT INTO POLICY VALUES (?, ?, ?);", (int(entry[0]),entry[1],entry[2]))
        conn.commit()

class Update_Policy_Form():
    def __init__(self):
        new = Tk()
        new.title("updating An Element In the POLICY DataBase")
        label = ttk.Label(new,text="update Policy window\nThese OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  update   ",command=self.update_policy_fn)
        update.pack()
        new.mainloop()


    def update_policy_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()

class Delete_Policy_Form():
    def __init__(self):
        new = Tk()
        new.title("Deleting An Element In the Policy DataBase")
        label = ttk.Label(new,text="Delete policy window\nThese OPERATIONS have to be implemented under the\n authorised people surveilance\n Enter the command to update the element")
        label.pack()
        self.e1 = ttk.Entry(new,width=100)
        self.e1.pack(padx=30,pady=30)
        update = ttk.Button(new,text="  Delete   ",command=self.delete_policy_fn)
        update.pack()
        new.mainloop()


    def delete_policy_fn(self):
        entry = self.e1.get()
        conn.execute(entry)
        conn.commit()




root = Tk()
root.title("Accident Rescue And Immediate Intimation SOFTWARE ")
app = UserInfo(root)
root.mainloop()
