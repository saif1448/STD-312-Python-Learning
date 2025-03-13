# 1---- 100
# print every prime number in this range


for num in range(1,101):
    isPrime = True
    for div in range(2, num):
        if num % div == 0:
            isPrime = False
            # print(f"{num} is not a Prime Number")
            break
    if isPrime:
        print(f"{num}", end=", ")


