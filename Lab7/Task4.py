import csv

file_path = "staff.csv"

with open(file_path, 'rt', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['name']}, Home Address: {row['home_address']}")