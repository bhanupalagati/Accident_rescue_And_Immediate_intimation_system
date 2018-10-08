"""
this python program is like a database connector.
There are three base tables in the accident service DB
User Db [Userid, UserEmail, HospitalId, policyid, Name, Age, Gender, City]

Hospital DB [HospitalId, HospitalEmail, HospitalName]

Policy Db [policyid, PolicyEmail, PolicyProvider]
"""

import sqlite3 #this is DB package

conn = sqlite3.connect('accident.db')

print("database has created successfully")


# # THIS IS THE USER TABLE
# conn.execute('''CREATE TABLE USER
#             (USERID INT PRIMARY KEY NOT NULL,
#             USEREMAIL TEXT NOT NULL,
#             HOSPITALID INT NOT NULL,
#             POLICYID INT NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             GENDER TEXT NOT NULL,
#             CITY TEXT NOT NULL);''')
#
#
# # THIS IS THE HOSPITAL TABLE
# conn.execute('''CREATE TABLE HOSPITAL
#             (HOSPITALID INT PRIMARY KEY NOT NULL,
#             HOSPITALEMAIL TEXT NOT NULL,
#             HOSPITALNAME TEXT NOT NULL);''')
#
#
#
# # THIS IS THE POLICY TABLE
#
# conn.execute('''CREATE TABLE POLICY
#             (POLICYID INT PRIMARY KEY NOT NULL,
#             POLICYEMAIL TEXT NOT NULL,
#             POLICYNAME TEXT NOT NULL);''')
#
#
#
#
#
# # TESTING THE VALUE INSERTION IN THE CREATED TABLES
# conn.execute("INSERT INTO USER (USERID,USEREMAIL,HOSPITALID,POLICYID,NAME,AGE,GENDER,CITY) \
#     VALUES (1,'bhanupalagati@gmail.com',1,1,'Bhanu_Palagati',20,'Male','Chennai')");
#
# conn.execute("INSERT INTO USER (USERID,USEREMAIL,HOSPITALID,POLICYID,NAME,AGE,GENDER,CITY) \
#     VALUES (2,'kingpavan.mandi@gmail.com',2,2,'Pavan_Mandi',20,'Male','Chennai')");
#
# conn.execute("INSERT INTO HOSPITAL (HOSPITALID,HOSPITALEMAIL,HOSPITALNAME) \
#     VALUES (1, 'lalatlochan68@gmail.com','chettinad_health_city')");
#
# conn.execute("INSERT INTO HOSPITAL (HOSPITALID,HOSPITALEMAIL,HOSPITALNAME) \
#     VALUES (2, 'bhanupalagati000@outlook.com','narayana_super_speciality_hospital')");
#
# conn.execute("INSERT INTO POLICY (POLICYID,POLICYEMAIL,POLICYNAME) \
#     VALUES (1, 'hitscsec@gmail.com','HDFC_ERGO')");
#
# conn.execute("INSERT INTO POLICY (POLICYID,POLICYEMAIL,POLICYNAME) \
#     VALUES (2, 'kingpavan.mandi@gmail.com','ICICI')");
# conn.commit()


# # DROPING THE CREATED TABLES
# cursor = conn.cursor()
# cursor.execute("DROP TABLE USER")
# cursor.execute("DROP TABLE HOSPITAL")
# cursor.execute("DROP TABLE POLICY")
# conn.commit()

# TESTING THE SELECT AND RETRIVAL OPERATIONS

cursor = conn.execute("SELECT * from USER")

for row in cursor:
    for col in row:
        print(col)
