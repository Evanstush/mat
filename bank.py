

print("Welcome to Tush bank💸💰🤑.\nHow may I help you?")
usernames = []
passwords = []
balances = []

while True:
    num = input(" 1.Create an account \n 2.Login \n ")
    if num == "1":
        print("Create an account\n")
        username= input("Enter your username: \n")
        password = input("Enter your password: \n")
        password_confirm = input("Confirm your password: \n")
        if password == password_confirm:
            usernames.append(username)
            passwords.append(password)
            balances.append(0.0)
            print("you have successfully created your account\n")
            continue
        else:
            print("your password and your password did not match\n")
            continue

    elif num == "2":
        print("login")
        enter_username = input("Enter your username: \n")
        enter_password = input("Enter your password: \n")
        if enter_username in usernames:
            index = usernames.index(enter_username)
            if passwords[index] == enter_password:
                print("you have successfully logged in\n")
                bal= balances[index]

                while True:
                    print("1. Deposit")
                    print("2. withdraw")
                    print("3. Transact")
                    print("4. Show balance")
                    print("5. logout")
                    choice = input("Enter your choice: \n")

                    if choice == "1":
                        print("Your account balance is: ",bal)
                        depo=int(input("Enter amount to deposit: \n"))
                        if depo < bal:
                            print("Enter a valid deposit\n")
                            continue
                        else:
                            bal=depo+bal
                            balances[index] = depo
                            print("Deposit Successful")
                            print("your account balance is: ",bal)

                    elif choice == "2":
                        withdraw=int(input("Enter amount to withdraw: \n"))
                        if withdraw < bal:
                            bal -= withdraw
                            balances[index] = bal
                            print("Withdraw Successful")
                            print("You have withdrawn ", withdraw)
                            print("your account balance is: ", bal)
                            continue
                        else:
                            print("insufficient funds\n")
                            print("Your account balance is: ",bal)
                            continue

                    elif choice == "3":
                        print("1. Phone number ")
                        print("2. To another bank")
                        num = input("choose where to transfer money: \n")
                        if num == "1":
                            phone = input("Enter your phone number: ")
                            amount = int(input("Enter amount to transfer: "))
                            if amount > bal:
                                print("insufficient funds\n")
                                print("Your account balance is: ", bal)
                                continue

                            else:
                                bal -= amount
                                balances[index] = bal
                                print("You have successfully transferred money to",phone)
                                print("Your balance is: ",bal)
                                continue
                        else:
                            bank = input("Enter your bank name: ")
                            acc = input("Enter your account number: ")
                            name = input("Enter your name: ")
                            amount = int(input("Enter amount to transfer: "))
                            if amount > bal:
                                print("insufficient funds")
                                continue
                            else:
                                    bal -= amount
                                    balances[index] = bal
                                    print("You have successfully transferred money to", bank, acc, name)
                                    print("Your balance is: ", bal)
                    elif choice == "4":
                        print("your balance is: ",bal)
                        continue

                    elif choice == "5":
                        print("you are logged out\n")
                        break
            else:
                print("Wrong input please try again")
                continue




        else:
            print("Wrong username or Password")
            continue
    else:
        print("Wrong choice")
        continue