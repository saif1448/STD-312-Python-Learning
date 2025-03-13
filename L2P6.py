
min = int(input("Enter min value: "))
max = int(input("Enter max value: "))

sum = 0

for i in range(min, max+1):
    if i%2 == 0:
        sum += i


print(f"The summation is {sum}")