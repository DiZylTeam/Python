# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# ==== МОЁ РЕШЕНИЕ ====

# не подходит для первых чисел, если они меньше чем i/2-1

list_1 = [8, 7]
k = 6

nearest_number = 0
diff_1 = k
diff_2 = 0
for i in list_1:
    if i <= k:
        temp = k - i
        if temp < diff_1:
            diff_1 = temp
            nearest_number = k - diff_1
    if i >= k:
        diff_2 = i - k
        if diff_2 <= diff_1:
            diff_1 = diff_2
            nearest_number = k + diff_1
print(f"{nearest_number}")



# ==== РЕШЕНИЕ GeekBrains ====

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)



