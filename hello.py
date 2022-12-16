import sqlite3
while True:
    print("\n\t\t\t\twrite exit for terminate session")
    
    name=input("\nEnter your name : ")
    if name=="exit":
        break
    
    enno=input("Enter your Enrollment Number : ")
    if enno=="exit":
        break
    
    year=input("Enter year of pursuing : ")
    if year=="exit":
        break
        



# a=sqlite3.connect('admin.db')

# mycursor=a.cursor()
# query='CREATE TABLE IF NOT EXISTS admin(id integer)'
# mycursor.execute(query)

# database="""INSERT INTO admin(id) values (512)"""
# mycursor.execute(database)
# a.commit()

# exe1='SELECT * FROM admin'
# mycursor.execute(exe1)

# data=mycursor.fetchall()
# print(data)