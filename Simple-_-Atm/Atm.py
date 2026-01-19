 # User Data
AccountBalance = 10000
userpin = 11223


#Entering the pin

pin =int(input("Enter your pincode: "))
if (pin != userpin):
    print("Invalid pin , You cant Login")

else:
    print("\n Login successfully ")


    while True:
        print("     ATM MENUE     ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("choose your option (1-4) :")

        if(choice == "1"):
            print(f"You current balance is:  ${AccountBalance} ")

        elif(choice == "2"):

            amount = int(input("Enter the amount you want to Deposit: "))    

            if(amount > 0):
                print(f"Before deposit: {AccountBalance}")  # DEBUG LINE
                AccountBalance += amount
                print(f"After deposit: {AccountBalance}")   # DEBUG LINE
                print(f"${amount} Deposited successfully.New Balance is ${AccountBalance}")

            else:
                print("invalid amount")    



        elif(choice == "3"):
            amount = int(input("Enter the amount you want to withdraw :"))     

            if(0 < amount<= AccountBalance):
                AccountBalance -= amount
                print(f"${amount} withdrawn successfully.Remaining Balance is ${AccountBalance}")

            else:
                print("Invalid Amount")




        elif(choice == "4"):
            print(f"Your Total Account Balance is {AccountBalance}")
            print("Exiting Atm\nThankyou for using our service ")
            break


        else:
            print("Invalid choice.Please Try again ")











