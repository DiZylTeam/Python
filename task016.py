# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i
# . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1


import random
number = int(input("Enter a number (array's length): "))
sp = []
i = 1
count = 0
while i <= number:
    sp.append(random.randint(1, 10))
    i += 1
print(sp)
x = int(input('Enter a number to find: '))
for i in sp:
    if x == i:
        count += 1
print(count)



# ==== ДЛЯ ПОИСКА ЦИФРЫ В ЧИСЛАХ ОТ 0 ДО 99 ====

# number = int(input('Enter a number: '))
# sp = []
# i = 1
# count = 0
# while i <= number:
#     sp.append(i)
#     i += 1
# print(sp)
# x = int(input('Enter a digit to find: '))
# sp_2 = []
# for j in sp:
#     if j < 10:
#         sp_2.append(j)
#     else:
#         sp_2.append(j // 10)
#         sp_2.append(j % 10)
# for k in sp_2:
#     if k == x:
#         count += 1
# print(count)


