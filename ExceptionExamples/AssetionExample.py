
def get_square(number):
    return number * 3


def test_get_square():
    assert get_square(2) == 4
    print(get_square(2))


try:
    test_get_square()
except AssertionError as e:
    print("Testing is Failed")
else:
    print("Testing is Passed")