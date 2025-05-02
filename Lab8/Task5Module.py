from math import inf


def avg_main(a, b):
    assert 1 <= a <= 9 and 1 <= b <= 9, f"Either value of a or b is out of range 1 to 9"
    avg = (a + b) / 2
    return avg


def find_largest_number(number_list):
    largest_number = float(-inf)
    for num in number_list:
        assert 1 <= num <= 9, "Input Number is out of range 1 to 9"
        if num > largest_number:
            largest_number = num
    return largest_number


