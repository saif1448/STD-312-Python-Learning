
def convert_fer_to_cel(input_temp_fer):
    cel = (input_temp_fer - 32) * 5 / 9
    return cel


def convert_daily_fer_temp():

    while True:
        input_temp_fer = input("Input Fahrenheit: ")
        if input_temp_fer == "end":
            return False
        else:
            input_temp_fer = float(input_temp_fer)
            if not (input_temp_fer >= -60 and input_temp_fer <= 130):
                print("Invalid input! Enter correct temperature! ")
                continue
            else:
                cel = convert_fer_to_cel(input_temp_fer)
                print(f"Celsius: {cel:.3f}")
                return True


