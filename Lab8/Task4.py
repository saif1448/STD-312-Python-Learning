import csv

file_path = "staff.csv"

try:
    with open(file_path, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                staff_id = row["staff_id"]
                if staff_id == '':
                    raise ValueError("Staff Id Not Found")
                print(f"Name: {row['name']}, Home Address: {row['home_address']}")
            except ValueError:
                print(f'Staff id is missing for the record')
except FileNotFoundError:
    print(f"File {file_path} not found.")
