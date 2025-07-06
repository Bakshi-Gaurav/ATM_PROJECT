#ATM PROGRAM
Name="gaurav"
Password="1"
user_name=input("Enter the User Name:")
Passwords=input("Enter the Password:")
s='''
    1. Credit
    2. Debit
    3. Mini Statement
    4. Exit
'''
Amount=2000
if Name==user_name and Passwords==Password:
    while True:
        print(s)
        option=int(input("enter the Option:"))
        if option==1:
         credit_amount=float(input("Enter The Amount"))
         print("Amount After credit",Amount+credit_amount)
        elif option==2:
         Debit_amount=float(input("Enter The Amount"))
         print("Amount After Debit",Amount-Debit_amount)
        elif option==3:
         print("Account Mini Statement:",Amount)
        elif option==4:
          break
else:
    print("Incorrect User Name and Password")