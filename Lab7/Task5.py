import csv

file_path = "staff.csv"

def print_csv_file():
    with open(file_path, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['staff_id']} Name: {row['name']}, Phone: {row['phone_number']} Home Address: {row['home_address'], }")


def add_staff_data(staff_data_row):
    with open(file_path, "a+", newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(staff_data_row)


while True:
    choice = input("Enter your choice: "
                       +"\n1. Add New Staff Data"
                       +"\n2. Print All Staff Data"
                       +"\n3. Exit Program\n")
    if choice == "1":
        id = input("Enter Staff ID: ")
        name = input("Enter Staff Name: ")
        phone = input("Enter Staff Phone Number: ")
        home_address = input("Enter Staff Home Address: ")
        staff_data_row = [id, name, phone, home_address]
        add_staff_data(staff_data_row)
    elif choice == "2":
        print_csv_file()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
