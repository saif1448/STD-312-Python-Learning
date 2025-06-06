import csv

file_path = "staff.csv"

with open(file_path, 'rt', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['name']}, Home Address: {row['home_address']}")

# with open(file_path, mode='rt', newline='', encoding='utf-8-sig') as csvfile:
#     redader = csv.reader(csvfile)
#     header = next(redader)
#     for row in redader:
#         print(f'Name: {row[1]}, Add: {row[3]}')