from ExceptionExamples.CustomValueError import CustomValueError


def return_division_result(a, b):
    return a / b

def return_multiplication_result(a, b):
    return a * b

def return_addition_result(a, b):
    return a + b

def return_subtraction_result(a, b):
    return a - b


while True:

   try:
       choice = input("1. Division\n"
                      "2. Multiplication\n"
                      "3. Addition\n"
                      "4. Subtraction\n"
                      "5. Exit\n")
       if choice == "1":
           try:
               a = int(input("Enter the first number: "))
               b = int(input("Enter the second number: "))
               result = return_division_result(a, b)
               print(result)
           except IndexError:
               print("Index Error")
               print("Try again!")
           except ZeroDivisionError:
               print("Division Error")
               print("Try again!")
           except ValueError:
               print("Value Error")
               print("Try again!")
           except Exception as e:
               print(e)
           else:
               print("There is no error while taking input!")
           finally:
               print("Operation has been completed!")
       elif choice == "2":
           result = return_multiplication_result(1, 2)
           print(result)
       elif choice == "3":
           result = return_addition_result(1, 2)
           print(result)
       elif choice == "4":
           result = return_subtraction_result(1, 2)
           print(result)
       elif choice == "5":
           break
       else:
           raise ValueError("The choice is not between 1 and 5")

   except ValueError as e:
        print(e)
