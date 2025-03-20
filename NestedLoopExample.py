# 2 line ----> outer loop
# 4 line ----> inner loop

set_a = ['A','B','C', 'D'] # 4
set_b = [1,2,3,4,5,6] # 6

for letter in set_a: # this the outer loop
    # print(letter)
    for num in set_b: # this is the inner loop
        # print(num)
        print(f"( {letter} X {num} )")


# if outer loop runs n times
# if inner loop runs m times

# total number of repeated task will be n*m times
# for each value of n, inner loop will run m times




