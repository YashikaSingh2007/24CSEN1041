balance=int(input("Enter the bank balance:"))

while True:
    print("\n ATM MENU")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=input("Enter your choice(1-4):")

    if choice=="1":
               print("Your Balance is rupees", balance)
    elif choice=="2":
               amount=int(input("Enter deposit amount:"))
               if amount> 0:
                  balance+=amount
                  print("Rupees",amount,"deposited successfully")
               else:
                   print("Invalid amount")
    elif choice=="3":
        amount=int(input("Enter withdrawal amount:"))
        if amount>balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Invalid amount")
        if amount<=balance:
            balance-=amount
            print("rupees",amount,"withdrawn successfully")
    elif choice=="4":
               print("Thank you")
               break
            
    else:
       print("Invalid choice! Please enter again")
                   
