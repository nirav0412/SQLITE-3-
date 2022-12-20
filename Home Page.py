import os
import Sec_page
print("\n\n\t\t\t\t\t\t\tWelcome to Expense Management System")
print("\t\t\t\t\t\t\t------------------------------------")

print("\n\n**required user login to gets benifits of EMS")

userid=int(input("\n\nEnter Userid :- "))
pwd=int(input("Enter Password :- "))

if userid==11 and pwd==11:
    os.system("cls")
    Sec_page.nik()
    
