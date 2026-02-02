#Expense Tracker Console Based



expenses = []
#Creating menu function
def menu():
    print('    💵NYC Expense Tracker    ')
    print('1:Add Expenses')
    print('2:View Expenses')
    print('3:Spending Analysis')
    print('4:Exit')

def add_expense():
    date = input('Enter the Date: ')
    amount = float(input('Enter the Amount You want to add:'))
    category = input('Enter the Category of Expense:')
    description = input('Enter a brief description: ')

    stored = {
        'date': date,
        'amount': amount ,
        'category': category,
        'description': description  
    }
    expenses.append(stored)
    print('✅ Expense added successfully')
    
    with open('ExpensesList','a') as file:
        file.write(str(stored)+ '\n')


def view_expenses():
    print('💵Following are Your Expenses... ')
    if not expenses:
        print('No Expenses Recorded')

    else:
        for item in expenses:
            print( 'Date:',item['date'])
            print('Amount$',item['amount'])
            print( 'Category:',item['category'])
            print('Description:',item['description'])

def spending_analysis():
    if not expenses:
        print('❌ No expenses to analyze')
        

    total_spent = 0
    category_spending = {}

    for item in expenses:
        amount = item['amount']
        category = item['category']

        total_spent += amount

        if category in category_spending:
            category_spending[category] += amount
        else:
            category_spending[category] = amount

    print('\n📊 Spending Analysis')
    print('-------------------')
    print(f'Total Spent: ${total_spent}')

    print('\nCategory-wise Spending:')
    for cat, amt in category_spending.items():
        print(f'{cat}: ${amt}')

    
while True:
    menu()
    choice = int(input('Enter Your choice: '))
    
    if choice == 1 :
        add_expense()

    elif choice == 2 :
        view_expenses()

    elif choice == 3 :
        spending_analysis()
        
    else :
         print('Goodbye,Thanks For using our Service')
         break
    
    