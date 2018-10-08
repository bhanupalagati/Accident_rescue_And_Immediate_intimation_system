# Accident_rescue_And_Immediate_intimation_system
This is a implementation of the smart accident rescue software where every vehicle get attached with a GPS device that can be already
available.
If any accident occured then the GPS device get acivated and then this will communicate with the satellite along with acknowledging all the mails attached with it like
Family
Hospital and Ambulance Service 
Policy and Insurance service

Here in place of a gps system a Key input is used if you press help in the GUI this will fetch all the data corresponding to that user and intimate the hospital and policy to which they are subscribed 


main.py is the root file connecting all the modules in the project which uses tkinter GUI
db_connector.py is responsible for  the creation and the update of the database
data_access.py is responsible for accessing the data in the database
mycontacts.txt will get updated with the mails to which we have to send mails
message.txt will get updated with the message what we have to send to the mails in the contacts
send_mail.py this will get data from the above two files and send mails 

*******************************************END******************************************************
