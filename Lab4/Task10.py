

def print_triangle(n):
    for num in range(n+1, 0, -1):
        string_val = ''
        for i in range(1, num):
            string_val += str(i)
        print(string_val)



while True:
    n = input("Enter value of n: ")
    if n == "stop":
        print("The program has been ended!")
        break
    n = int(n)
    print_triangle(n)
