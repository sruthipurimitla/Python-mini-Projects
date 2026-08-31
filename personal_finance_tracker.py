#Personal expense tracker project

expensesList = [] #list of expenses in form of dictionary
print("WELCOME TO THE EXPENSE TRACKER")

while True:
    print("********MENU**********")
    print("1. add expenses")
    print("2. view  all expenses")
    print("3. view total expenses")
    print("4. exit")

    choice = int(input("please enter your choice:"))

    #1. add expenses
    if(choice == 1):
        date=input("when did you spend the money?")
        category=input("on which did you spend the money?")
        description=input(" any other details?")
        amount=float(input("enter the amount you spent:"))

        expenses={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expenses)
        print("\n DONE BRO. Expenses are added successfully")

    #2. view  all expenses
    elif(choice==2):
        if(len(expensesList)==0):
            print("no Expenses are added ")
        else:
            print("---------your all spendings--------")
            count=1
            for eachspending in expensesList:
                print(f"spending number{count}->{eachspending['date']},{eachspending['category']},{eachspending['description']},{eachspending['amount']}")
                count=count+1

    #3. view total expenses
    elif (choice==3):
        total=0
        for eachspending in expensesList:
            total =total+eachspending["amount"]

            print("\ntotal spending=",total)

    #4.exit
    elif(choice == 4):
        print("THANK YOU . you are out of the tracker")
        break

    else:
        print("INVALID CHOICE!!!!.\n try again")