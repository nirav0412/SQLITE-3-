import sqlite3
a=sqlite3.connect("ems.db")
c=a.cursor()

def getamount():
    query='''SELECT sp_uspend FROM expen''' 
    c.execute(query)
    amount=c.fetchall()
    bal=int(amount[0][0])
    print(bal)
def nik():
    print("\n\n\t\t\t\t\t\t\tWelcome to Expense Management System")
    print("\t\t\t\t\t\t\t------------------------------------")

    print("\n***you are successfully loging in")
    spend=10
    print('''\n\n\tHere is Your Total Spend 
                                    
                    %d''' %spend)

    print('''\n\n\tHere is Your Total Save 
                                    
                    %d''' %spend)

    print('''\n\n\tHere is Your Total Amount in Wallet 
                                    
                    %d''' %spend)

    print('''Choose number for perform operatiom
            
            1.For Enter Spend
            2.For Enter Save
            3.For Transaction History
            4.For Perform Delete and Edit in data
            5.For Logout''')

    num=int(input("Enter Your Choice"))

    if num==1:
        cus1=input("\tEnter a Customer Name : ")
        spend1=int(input("\tEnter amount that you spend : "))
        date=input("\tEnter date of Transaction : ")
        
        if spend1<=0:
            print('Enter Valid Amount !!')
        else:
            spend=spend+spend1
    print("\n\n\t\t\t\t\t\t\tThank you for using Expense Management System")
    print("\t\t\t\t\t\t\t---------------------------------------------")



    def crt_table():
        c.execute('CREATE TABLE IF NOT EXISTS expen(sp_cuname TEXT,sp_uspend INTEGER,sp_dospend INTEGER)')



    def data():
        crt_table()
        c.execute('INSERT INTO expen VALUES(?,?,?)',(cus1,spend1,date))
        a.commit()

        c.execute('SELECT * FROM expen')

        print(c.fetchall())
    data()
    # how can i print data from database to place where i want to print
    # delete and edit and update

    getamount()
if __name__=="__main__":
    nik()