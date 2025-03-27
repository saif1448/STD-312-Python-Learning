
#isalpha() ---> if the character is an alphabet
#isnumeric() ---> if the character is a numeric digit
#isdigit() ---> if the character is a digit


def extract_numbers(input_str):

    extracted_number_str = ""

    for num in input_str:
        if num.isdigit():
            extracted_number_str += num

    if extracted_number_str == "":
        return 0
    else:
        extracted_number = int(extracted_number_str)
        return extracted_number


while True:
    input_str = input("Enter the string: ")
    if input_str == "stop":
        print("The program is being stopped")
        break
    extracted_number = extract_numbers(input_str)
    print(f"The extracted number is: {extracted_number}")

