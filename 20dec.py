import sqlite3

a=sqlite3.connect("nirav.db")
c=a.cursor()

def crt_table():
    c.execute('CREATE TABLE IF NOT EXISTS expen(spend INTEGER,save INTEGER,wallet INTEGER)')



def data(ex1,ex2,ex3):
    crt_table()
    c.execute('INSERT INTO expen VALUES(?,?,?)',(ex1,ex2,ex3))
    a.commit()

    c.execute('SELECT * FROM expen')

    print(c.fetchall())

ex1=int(input('enter a num : '))
ex2=int(input('enter a num : '))
ex3=int(input('enter a num : '))

data(ex1,ex2,ex3)