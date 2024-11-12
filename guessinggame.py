import random


while True:
    num = random.randint(1, 9)
    choice = input("Enter a random number😊\n")
    if choice.isdigit():
        choice = int(choice)
        if 0<=choice<=9:
            if choice == num:
                print(num)
                print("Correct! Get your prize\n")
                play = input("Do you want to play again? (y/n)")
                if play == "y":
                    continue
                elif play == "n":
                    break
                else:
                    print("Invalid input")
                    continue
            else:
                print(num)
                print("Try again! Name your prize!!!\n")
                continue
        else:
            print("Enter a number between 0 and 10\n")
            continue
    else:
        print("Enter a whole number\n")
        continue


