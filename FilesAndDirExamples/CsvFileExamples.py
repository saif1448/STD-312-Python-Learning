
# first we are gonna use the open()
# use t ---> to indicate text orientation
# newline='' ---> to avoid new line issues
# encoding='utf-8-sig' ---> to avoid encoding issues

# we have csv module to perform operations on csv files

import csv

# as works to indicate aliasing

with open('Sample.csv', 'rt', newline='', encoding='utf-8-sig') as csvfile:
    # output_str = csvfile.read()
    # print(output_str)
    reader = csv.reader(csvfile) # reader function is gonna return the row as a list
    header = next(reader)
    for row in reader:
        print((row[1], row[2])) # and because of this, we can index the the values in the row


with open('Sample.csv', 'rt', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile) # this function is returning a dictionary
    for row in reader:
        print((row['name'], row['id'])) # we can access the row individual values by using the dic key




