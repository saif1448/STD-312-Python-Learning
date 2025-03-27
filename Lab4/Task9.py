from Task9Module import get_next_character, reverse_string, extract_numbers, shift_string

while True:
    choice = int(input("Choose one of the below options: (1-5): "
                   "\n1. Get Next Character"
                   "\n2. Reverse String"
                   "\n3. Extract Numbers from String"
                   "\n4. Shift a String"
                   "\n5. Stop the program\n"))

    if choice == 1:
        char = input("Enter a character: ")
        next_char = get_next_character(char)
        print(f"The next character is: {next_char}")
    elif choice == 2:
        input_str = input("Enter a string: ")
        reversed_string = reverse_string(input_str)
        print(f"The reversed string is: {reversed_string}")
    elif choice == 3:
        input_str = input("Enter a string: ")
        extracted_numbers = extract_numbers(input_str)
        print(f"The extracted numbers is: {extracted_numbers}")
    elif choice == 4:
        input_str = input("Enter a string: ")
        shifted_string = shift_string(input_str)
        print(f"The shifted string is: {shifted_string}")
    elif choice == 5:
        print("The program has ended")
        break
    else:
        print("Invalid choice")
