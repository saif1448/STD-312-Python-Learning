import csv
def read_sales_data(file_path):
    sales_data = {}

    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    date = row['date']
                    product = row['product']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    total_value = price * quantity

                    if product in sales_data:
                        sales_data[product] += total_value
                    else:
                        sales_data[product] = total_value

                except ValueError as e:
                    print(f"Skipping row due to data error: {row} => {e}")

        return sales_data

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return {}

def print_sales_summary(sales_data):
    if not sales_data:
        print("No sales data to display.")
        return
    print("Total Sale Value per Product in 2022:")
    for product, total in sales_data.items():
        print(f"{product}: ${total:.2f}")

file_path = "sales_2022.csv"  # Update this path as needed
sales_summary = read_sales_data(file_path)
print_sales_summary(sales_summary)
