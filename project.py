print("------ Welcome to the python Bill payment application ------")
history = []
while True:
    try:
        print("1. Pay Bill")
        print("2. View Bill History")
        print("3. Delete Bill History")
        print("4. Exit")
        select = int(input("Please select an option = "))
        if select == 1:
            bill_amount = int(input("Enter bill amount: "))
            pay_amount = int(input("Enter payment amount: "))
            history.append((bill_amount, pay_amount))
            if bill_amount > pay_amount:
                print("Payment amount is less than bill amount. Please try again.")
                pay_amount = int(input("Enter payment amount: "))
            elif bill_amount < pay_amount:
                print("You pay are more amount. I calculate your bill and give you the remaining amount.")
                remaining_amount = pay_amount - bill_amount
                print(f"Your remaining amount is: {remaining_amount}")
            elif bill_amount == pay_amount:
                print("Bill paid successfully!")

        elif select == 2:
            print(history)

        elif select == 3:
            history.clear()
            print("Bill history deleted successfully!")
    
        elif select == 4:
            print("Exiting the application. Goodbye!")
            break

        elif select == "":
            print("No option selected. Please select a valid option.")
        
        else:
            print("Invalid option. Please select a (1-4).")
    except ValueError:
        print("An error occurred. Please try again.")