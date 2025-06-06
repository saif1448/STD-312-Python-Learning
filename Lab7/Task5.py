import csv

file_path = "staff_n.csv"

# this is if the file is newly created, intially create the headers for the csv
# header = ['staff_id','name','phone_number','home_address']
#
# with open(file_path, mode='w', newline='', encoding='utf-8-sig') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)

def print_csv_file():
    with open(file_path, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['staff_id']} Name: {row['name']}, Phone: {row['phone_number']} Home Address: {row['home_address'], }")


def add_staff_data(staff_data_row):
    with open(file_path, "a+", newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(staff_data_row)

# def add_staff_data(staff_data_row):
#     with open(file_path, "a+", newline='', encoding='utf-8-sig') as file:
#         # writer = csv.writer(file)
#         # writer.writerow(staff_data_row)
#         headers = ['staff_id','name','phone_number','home_address']
#         writer = csv.DictWriter(file, fieldnames=headers)
#         writer.writerow(staff_data_row)


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
        # staff_data_row = {
        #     'staff_id': id,
        #     'name': name,
        #     'phone_number': phone,
        #     'home_address': home_address,
        # }
        add_staff_data(staff_data_row)
    elif choice == "2":
        print_csv_file()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
