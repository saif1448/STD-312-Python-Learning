

watch_collection = {
    "rolex" : 100,
    "omega" : 150,
    "pudor" : 135,
    "patet" : 245
}

total_cost = 0.0

while True:

    watch_name = input("Choose one of the watches: \nrolex \nomega \npudor \npatet and enter 'end' to end\n")

    if watch_name == 'end':
        break

    watch_price = watch_collection[watch_name]

    total_cost += watch_price + (watch_price*5/100)

    print(f'After adding the watch {watch_name}  total price is {total_cost}')


print(f"Total Price is {total_cost}")

