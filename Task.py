#
# l1 = [1001, 60, 65, 55, 59, 'P']
# l2 = [1002, 80, 75, 68, 72, 'D']
# l3 = [1003, 45, 50, 52, 50, 'P'] # 1d list
#
# student_data = [l1, l2, l3]  # list of list
#
# # std_marsk ---> this is list is carrying some 1d list
# # that is why std_marks is a 2d list
#
# # A 2d list is a list of 1d list
#
#
# # 3d ---> A 3d list will be a list of 2d list
#
# # 4d ---> a 4d list will be a list of 3d list
#
# # nd ---> a nd list will be a list of (n-1)d list
#
#
# # 1002 ---> grade [1][5]
#
# # print(std_marks[1][5])
# # print(std_marks[2][4])
#
# # it is gonna print each student grade
# # std_marks = [l1, l2, l3]
# #std ---> l1 ---l2 ---- l3
# # for std in std_marks:
# #     print(f"{std[0]} ---> {std[4]}")
# #
#
# hd_grade_list = [[val for val in row if True  ]for row in student_data]
#
# print(hd_grade_list)

