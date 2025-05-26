def function_list (lista, listb):
    final_list = lista + listb
    return final_list

list1 = [1, 3, 5, 7, 9, 11]
list2 = [2, 4, 6, 8,10, 12]
#list3 = list2

final = function_list(list1, list2)
print(final)
# list1.remove(9)
# del list1[0]
print(list1.pop(2))
print(list1)
print(list1.pop())
list1.clear()
print(list1)
print(len(list2))
print(max(list2))
print(min(list2))

