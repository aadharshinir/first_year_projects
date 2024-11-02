while True:
    print("--------Items--------")
    print("1)Biscuit         Rate Rs.10/-")
    print("2)Chips            Rate Rs.5/-")
    print("3)Maaza            Rate Rs.15/-")
    print("4)Exit")
    print("Choose your preference(1/2/3/4): ")
    A = int(input())
    if A == 4:
        break
    elif A>4 or A<1:
        print("Invalid Choice")
        continue

    B = int(input("Enter the required quantity: "))
    product_name = ""
    if A == 1:
        product_name = "Biscuit"
    elif A == 2:
        product_name = "Chips"
    elif A == 3:
        product_name = "Maaza"
    
    if A == 1:
        amount = 10*B
        print("The amount is", amount)
        print("Select 4 to cancel.Select any number to continue the purchase")
        C = int(input())
        if C == 4:
            exit()
        else:
            user_amt = int(input("Insert the required amount: "))
    elif A == 2:
        amount = 5*B
        print("The amount is", amount)
        print("Select 4 to cancel.Select any number to continue the purchase")
        C = int(input())
        if C == 4:
            break
        else:
            user_amt = int(input("Insert the required amount: "))
    elif A == 3:
        amount = 15*B
        print("The amount is", amount)
        print("Select 4 to cancel.Select any number to continue the purchase")
        C = int(input())
        if C == 4:
            break
        else:
            user_amt = int(input("Insert the required amount: ")) 

    balance = amount - user_amt
    amt_paid = user_amt
    while balance>0:
        print("Balance amount is",balance,"Insert the balance amount or Select 4 to cancel the purchase")
        user_amt1 = int(input("Insert the required amount: "))
        balance = balance - user_amt1
        amt_paid = amt_paid + user_amt1
        
    if balance<0:
        print("Please take the balance amount Rs.",balance)

    while True:
        confirm = int(input("Would you like to make another purchase? Press 1 to continue or 0 to exit: "))
        if confirm < 0 or confirm > 1:
            print("Invalid input")
            continue
        elif confirm == 0:
            print("-------Receipt-------")
            print("Selected product - ", product_name)
            print("Quantity - ",B)
            print("Total amount = ", amount)
            print("Amount paid = ", amt_paid)
            print("Balance given = ",balance)
            print("Thank you for the purchase. Have a good day!")
            exit()
        elif confirm == 1:
                print("-------Receipt-------")
                print("Selected product - ", product_name)
                print("Quantity - ",B)
                print("Total amount = ", amount)
                print("Amount paid = ", amt_paid)
                print("Balance given = ",balance)   
        break
   