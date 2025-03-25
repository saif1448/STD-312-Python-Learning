

#modular programming ---> deviding the task into multiple section / multiple part
# creating separate python files or modules
# creating different functions

# import ---> it calls another python file which contains a lot of different functions
# i have to use dot operator


# import number_calculator
from number_calculator import get_avg_number, get_number_multi, get_largest_number

from unit_converter import convert_km_to_m, convert_m_to_km


def run_app():
    while True:
        choice = input("Choose one of the options from below (1-5): "
                       +"\n1. Get Average of two numbers"
                       +"\n2. Get Largest of two numbers"
                       +"\n3. Get Multiplication of two numbers"
                       +"\n4. Convert KM to M"
                       +"\n5. Convert M to KM"
                       +"\n6. END")

        if choice == '1':
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))
            # avg = number_calculator.get_avg_number(a, b)
            avg = get_avg_number(a, b)
            print(f"The average of {a} and {b} is {avg}")
        elif choice == '2':
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))
            # largest = number_calculator.get_largest_number(a,b)
            largest = get_largest_number(a, b)
            print(f"The largest number is {largest}")
        elif choice == '3':
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))
            # mult = number_calculator.get_number_multi(a,b)
            mult = get_number_multi(a, b)
            print(f"The multiplication of {a} and {b} is : {mult}")
            pass
        elif choice == '4':
            km = float(input("Enter value in KM: "))
            m = convert_km_to_m(km)
            print(f"{km} km converted to {m} m")
        elif choice == '5':
            m = float(input("Enter value in M: "))
            km = convert_m_to_km(m)
            print(f"{m} m converted to {km} km")
        elif choice == '6':
            print("Application Ended!")
            break
        else:
            print("Wrong choice! Try again!")



run_app()