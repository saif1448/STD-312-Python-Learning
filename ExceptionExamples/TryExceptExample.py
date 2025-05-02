

x = None
try:
    x  = int(input("Enter a number: "))
    if x < 20 or x > 50:
        raise ValueError("Enter a number between 20 and 50")
    print(f"Number: {x}")
except ValueError:
    print("Enter a number between 20 and 50")

x += 20

print(f"Number: {x}")

# if there is an possibility of using a variable declared in try-except block outside of the block
# then try to first declare and initialize that variable above and outside of the try-except block
# and then use that variable inside the try-except block and after outside the try-except block