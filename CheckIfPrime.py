# 2,3,5,7,11,13,17
# prime numbers are those
# they are divisible only by 1 and that number itself

#13 ----> 2-----12
#14 ----> 2 ---- 13 ----> (2,14) --- 2, 7
#25 ----> 2 ---- 24 ---> (2, 25)
#36 ----> 2 ---- 35 ----> (2,36)
# range ---> (min, max) -----
# 2 ---> num-1 +1 ===> num
# num ---> 2--- num-1 ---> (2,num)


num = int(input("Enter the number: "))

isPrime = True

for div in range(2,num):
    if num % div == 0:
        isPrime = False
        print(f"{num} is not a Prime Number")
        break

if isPrime:
    print(f"{num} is a Prime Number")



