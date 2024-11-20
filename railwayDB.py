
   
 #                                           RAILWAY MANAGEMENT SYSTEM

import mysql.connector  

#create database connection
connection=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345678",
    database = "railwaymanagement",
    auth_plugin="mysql_native_password",
    )

#to check the connection is established or not
if connection.is_connected():
    print("Connected to  Database")
else:
    print("Not Connected to Database")

    
# press 1 to book train : trainname , date , destination , userid
# press 2 to get all the details of the ticket
# press 3 to delete the train ticket
# press 4 to update the  details in train ticket
# press 5 to add one more ticket : passengername , passemail , passmobile ,passage , date,destination
# press 6 to get all the details of  the passenger
# press 7 to delete the ticket of the passenger
# press 8 to update the details  of passenger




Traindata="create table if not exists traindata( trainname text , date text , destination text, userid text)"
mycursor=connection.cursor()
mycursor.execute(Traindata)
connection.commit()


print("press 1 to book train")
print("press 2 to get all the details of the ticket")
print("press 3 to update the  details in train ticket")
print("press 4 to delete the train ticket")
print("press 5 to add one more ticket")
print("press 6 to get all the details of  the passenger")
print("press 7 to update the details  of passenger")
print("press 8 to delete the ticket of the passenger")

select=int(input("enter no. 1 to 8"))

#to book train
if(select==1):
    insertvalue="insert into traindata values('{}' , '{}' , '{}' , '{}')".format(input("enter train name ") , input("enter train date ") , input("enter destination ") , int(input("enter userid ")))
    mycursor.execute(insertvalue)
    connection.commit()

# to get all details
elif(select==2):
    mydetails = "select * from traindata"
    mycursor.execute(mydetails)
    print(mycursor.fetchall())
    connection.commit()

# to update the  train ticket
elif(select==3):
    updatedetails = "update traindata set trainname = 'vande bharat' ,date = '19.11.24' , destination = 'dehradun' where userid = '1'"
    mycursor.execute(updatedetails)
    connection.commit()

# to delete the  train ticket
elif(select==4):
    deleteticket = "delete from traindata where userid ='1'"
    mycursor.execute(deleteticket)
    connection.commit()
        
passengerdata = "create table if not exists passdata(passname text , passemail text , passmobile text , passage text , destination text , passengerid text)"
mycursor.execute(passengerdata)
connection.commit()

# to add the passenger data
if(select==5):
    insertpassdata = "insert into passdata values('{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(input("enter passenger name ") , input("enter passsenger email ") , int(input("enter passenger mobile no.")) , input("enter passenger age") , input("enter passsenger destination") , input("enter passenger id "))
    mycursor.execute(insertpassdata)
    connection.commit()    

# to get all passenger details
elif(select==6):
    passengerdata = "select * from passdata"
    mycursor.execute(passengerdata)
    print(mycursor.fetchall())
    connection.commit()


# to update the passenger data
elif(select==7):
    updatepassdata  = "update passdata set passage = '22' , destination =  'chennai' where passid = '1'"
    mycursor.execute(updatepassdata)
    connection.commit()

# to delete the passenger
elif(select==8):
    deletepassdata = "delete from passdata where passid = '1'"
    mycursor.execute(deletepassdata)
    connection.commit()
    
else:
    print("you have selected out of the range no")

