
input_ls = [1, 'cat', 2, 'cat', 2.3, 2]

def count_unique_list_element(input_list):
    temp_ls = []
    for element in input_list:
        found = False
        for val in temp_ls:
          if val is element:
              found = True
              break
        if not found:
            temp_ls.append(element)

    return (len(temp_ls), temp_ls)


unique_element_count, unique_element_list = count_unique_list_element(input_ls)

print(f"Unique element count: {unique_element_count} and unique element list: {unique_element_list}")

