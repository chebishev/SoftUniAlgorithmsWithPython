# reverse array
elements = input().split()
for left_index in range(len(elements) // 2):
    right_index = len(elements) - 1 - left_index
    elements[left_index], elements[right_index] = elements[right_index], elements[left_index]
print(elements)
# print(" ".join(elements))
# -----------------------------------------------------------------------------------

