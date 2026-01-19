from tkinter import *

root = Tk()
root.title('Dummy Atm')
root.geometry('800x600')

Account_pass = 2226
Account_Balance = 20000


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def login():
    clear_screen()

    Label(root, text='Enter Your pass key.', font=('Arial', 20)).pack(pady=20)
    pass_entry = Entry(root, font=('Arial', 20), show='*')
    pass_entry.pack()

    def login_check():
        user_input = pass_entry.get()
        if user_input != str(Account_pass):
            Label(root, text='Invalid passkey!', font=('Arial', 20), fg='Red').pack()
        else:
            menu()

    Button(root, text='Login', font=('Arial', 12), command=login_check).pack(pady=20)


def menu():
    clear_screen()

    Label(root, text='Welcome To Dummy ATM', font=('Arial', 24)).pack(pady=20)
    Button(root, text='Check Amount', font=('Arial', 12), width=15, command=check_balance).pack(pady=5)
    Button(root, text='Deposit Amount', font=('Arial', 12), width=15,command=deposit_money).pack(pady=5)
    Button(root, text='Withdraw Money', font=('Arial', 12), width=15,command=withdraw_money).pack(pady=5)
    Button(root, text='Exit', font=('Arial', 12), width=15, command=root.quit).pack(pady=5)


def check_balance():
    clear_screen()
    Label(root,text=f"Account Balance = ${Account_Balance}\n Thanks For Our service.",font=('Arial',20)).pack(pady=50)

def deposit_money():
    clear_screen()
    Label(root,text='Enter the Amount You want to deposit.',font=('Arial',20)).pack(pady=50)
    d_amount = Entry(root,font=('Arial',20))
    d_amount.pack()

    def deposit():

      global Account_Balance
      try:
            amount = float(d_amount.get())
            Account_Balance += amount
            Label(root, text=f"New Account Balance = ${Account_Balance}", font=('Arial', 15), fg='green').pack(pady=20)
      except:
            Label(root, text="Enter a valid number!", font=('Arial', 15), fg='red').pack(pady=20)

      
    Button(root,text='Deposit',font=('Arial',10),background='black',fg='green',command=deposit,padx=20).pack(pady=20)
    Label(root,text=f"New Account Balance = ${Account_Balance}")
    

def withdraw_money():
    clear_screen()
    Label(root, text='Enter the Amount You want to withdraw.', font=('Arial', 20)).pack(pady=50)
    w_amount = Entry(root, font=('Arial', 20))
    w_amount.pack()

    def withdraw():
        global Account_Balance
        try:
            amount = float(w_amount.get())
            if amount > Account_Balance:
                Label(root, text="Insufficient Balance!", font=('Arial', 15), fg='red').pack(pady=20)
            else:
                Account_Balance -= amount
                Label(root, text=f"New Account Balance = ${Account_Balance}", font=('Arial', 15), fg='green').pack(pady=20)
        except:
            Label(root, text="Enter a valid number!", font=('Arial', 15), fg='red').pack(pady=20)

    Button(root, text='Withdraw', font=('Arial', 10), bg='black', fg='green', command=withdraw).pack(pady=20)
    Button(root, text='Back to Menu', font=('Arial', 10), command=menu).pack(pady=10)

    




login()

root.mainloop()
