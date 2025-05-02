
from Task5Module import avg_main, find_largest_number

def testAvgMain(a, b, expected_value):
    try:
        output_val = avg_main(a, b)
        assert output_val == expected_value, f"Expected {expected_value}, but got {output_val}"
        print(f"Test passed for inputs ({a}, {b})")
    except AssertionError as e:
        print(f"Test failed for inputs ({a}, {b}): {e}")

def testFindLargestNumber(numberList, expected_value):
    try:
        largest_num = find_largest_number(numberList)
        assert largest_num == expected_value, f"Expected {expected_value}, but got {largest_num}"
        print(f"Test passed for inputs {numberList}")
    except AssertionError as e:
        print(f"Test failed for inputs {numberList}: {e}")



testAvgMain(10,4,7)
testAvgMain(4,2,3)
testAvgMain(3, 5, 4)
testAvgMain(9, 1, 5)
testAvgMain(14, 6, 10)
testAvgMain(7, 9, 8)

testFindLargestNumber([1, 2, 3], 3)
testFindLargestNumber([5, 5, 5], 5)
testFindLargestNumber([1, 10, 5], 10)
testFindLargestNumber([9, 2, 9], 9)
testFindLargestNumber([3, 4, 8, 6], 8)
testFindLargestNumber([0, 2, 3], 3)
testFindLargestNumber([2, 3, 4, 9], 9)
testFindLargestNumber([-1, 5, 6], 6)






