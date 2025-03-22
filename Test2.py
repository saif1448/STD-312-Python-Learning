
def add_two_number(a, b):
    print(f"The sum is {a+b}")


add_two_number(5,6)
add_two_number(11,29)
add_two_number(50,90)


def find_the_largest(a, b, c):
    if a > b:
        if a > c:
            print(f"{a} is the largest")
        else:
            print(f"{c} is the largest")
    else:
        if b > c:
            print(f"{b} is the largest")
        else:
            print(f"{c} is the largest")


find_the_largest(100,200,300)
find_the_largest(300,5000,1000)
find_the_largest(1000,600,900)


def say_greeings():
    print("Hi there!")

say_greeings()
say_greeings()
say_greeings()