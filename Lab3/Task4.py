
for num in range(10, 0, -1):
    string_val = ''
    for i in range(1,num):
        string_val += str(i)
    print(string_val)


#outer num = 10
# inner loop --- range ---> (1,10) ------> 1....9

# outer num = 9
# inner loop --- range ---> (1,9) -----> 1....8

#outer num = 8
# inner loop ---> (1,8) ----- 1....7
