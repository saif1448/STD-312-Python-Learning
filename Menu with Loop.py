# Very Basic calculator app
# Input two numbers
# Which operation to perform
# Addition, Subtraction, Multiplication, Division
# From user, we will ask to input infinitely unless exit command is given


# isApplicationRunning = True

while True:
    print("Enter Two Numbers")
    a = int(input("A: "))
    b = int(input("B: "))

    print("Choose one of the Arithmatic Operation to perform\n"
          + "1. Addition\n"
          + "2. Subtraction\n"
          + "3. Multiplicaton\n"
          + "4. Division\n"
          + "5. Exit\n"
          + "(1-5)\n")

    inp = int(input())

    if inp == 1:
        print(f"Addition Result is {a + b}")
    elif inp == 2:
        print(f"Subtraction Result is {a - b}")
    elif inp == 3:
        print(f"Multiplication Result is {a * b}")
    elif inp == 4:
        print(f"Division Result is {a / b}")
    elif inp == 5:
        # isApplicationRunning = False
        break
    else:
        print("Wrong Input Has Been Chosen!!\n")


print("Application has been terminated!")



