import sqlite3

while True:
    print('\n\t\t\t\t\t\t Write exit for Terminate Session')

    name=input('Enter your name :')
    if name =='exit':
        break

    enno=int(input("\nEnter your Enrollment Number : "))
    if enno=='exit':
        break

    year=int(input("\nEnter year of Pursuing : "))
    if year=="exit":
        break



a=sqlite3.connect("admin2.db")

mycursor=a.cursor()
query='CREATE TABLE IF NOT EXISTS admin2 (name TEXT,enno INTEGER,year INTEGER)'
mycursor.execute(query)

# database=''
mycursor.execute('INSERT INTO admin2(name,enno,year) VALUES (?,?,?)',(name,enno,year))
a.commit()

exe1='SELECT * FROM admin2'
mycursor.execute(exe1)

data=mycursor.fetchall()
print(data)