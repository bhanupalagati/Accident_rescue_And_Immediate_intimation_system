"""
Access the data based on the given input
"""

import sqlite3 #this is DB package

conn = sqlite3.connect('accident.db')

def data_retrive(userid):
    # this variable will collect the complete data
    msg = """--------------------------------------\n"""
    usercursor = conn.execute("SELECT * from User")

    # opening the contacts file and reseting the data in the file to process the other data
    filename = 'mycontacts.txt'
    with open(filename,'w'): pass

    # opening the message file and reseting the context as per the appropriate user
    msg_file_name = 'message.txt'
    with open(msg_file_name,'w'): pass

    # searching for the user using the user id then we retrive the other primary keys
    for row in usercursor:
        if row[0] == userid:
            for col in row:
                print(col)
                msg+=str(col)+"\n"
            print("**********************************************************")
            msg+="**********************************************************\n"
            file = open(filename,'w')
            file.write(row[4]+" "+row[1]+"\n")

            msg_file = open(msg_file_name,'w')
            msg_file.write("User_ID "+str(row[0])+"\n"
                            +"User_name "+row[4]+"\n"
                            +"AGE "+str(row[5])+"\n"
                            +"Gender "+row[6]+"\n"
                            +"City "+row[7]+"\n"
                            +"EmailId "+row[1])
            hospid = row[2]
            policyid = row[3]
            break

    hospcursor = conn.execute("SELECT * from HOSPITAL")

    for row in hospcursor:
        if row[0] == hospid:
            for col in row:
                print(col)
                msg+=str(col)+"\n"
            hospemail = row[1]
            print("**********************************************************")
            msg+="**********************************************************\n"
            file.write(row[2]+" "+row[1]+"\n")
            break

    policycursor = conn.execute("SELECT * from POLICY")

    for row in policycursor:
        if row[0] == policyid:
            for col in row:
                print(col)
                msg+=str(col)+"\n"
            policyemail = row[1]
            print("**********************************************************")
            msg+="**********************************************************\n"
            file.write(row[2]+" "+row[1]+"\n")
            break

    print("We successfully accessed and retrived the data from all the three cases")

    return msg
# data_retrive(3)
