
marks = [70, 50, 40, 80, 65, 75, 90, 55, 69]

# m = []
#
# for mark in marks:
#     if mark >= 70:
#         m.append(mark)
#
# print(m)

m = [val for val in marks if val >= 70]

print(m)