# ===================================
# Lesson 2
# Homework. Task 1
# ===================================
foo_list = list()
foo_list.append(None)
foo_list.insert(0, 0)
foo_list.insert(1, '1')
foo_list.insert(99, 9.9)
foo_list.append(1 + 2j)
foo_list.append(b'text')
foo_list.append(ZeroDivisionError)

foo_dict = {'k1':'v1', 'k2':'v2'}
foo_list2 = list(foo_dict)
foo_list2.append(foo_dict)
foo_list2.append({1,2,3})
foo_list2.append([4,5,6])
foo_list2.append((7,8,9))

foo_list.extend(foo_list2)

print(foo_list)
for el in foo_list:
    print(type(el))



