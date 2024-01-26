name = input("Enter your name: ")
password = input("Enter password: ")
balance = 0

while True:
    if len(password) == 10 and name == "Evans" and password == "1234567890":
        choice = input('SELECT:\n1: Check balance\n2: Deposit\n3: Check bonus\n4: Exit\nEnter your choice: ')

        if choice == "1":
            print("Hello %s, your balance is $%d" % (name, balance))
        elif choice == "2":
            deposit = int(input("Enter the amount: "))
            if deposit > 100:
                bonus = 100
                balance = balance + bonus + deposit
                print("Your total balance is $%d" % balance)
            else:
                balance = balance + deposit
                print("Your total balance is $%d" % balance)
        elif choice == "3":
            # You can implement bonus functionality here if needed
            print("No bonus available at the moment.")
        elif choice == "4":
            print("Exiting the program.")
            break  # Exit the loop
        else:
            print("Invalid choice.")
    else:
        print("Wrong password or username")

# The program will continue running until the user chooses to exit (entering '4').
