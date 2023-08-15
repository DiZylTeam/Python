# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:         Ввод:
# 5             5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:        Вывод:
# 0             2
# (каждое число вводится с новой строки)



# ОДНО РЕШЕНИЕ (закольцованный массив)

import random

def check_neighbours(index,array):
    if array[(index + 1) % len(array)] < array[index] and array[index - 1] < array[index]:
        return True




n = int(input("Введите кол-во элементов массива: "))
array = [random.randint(0, 10) for _ in range(n)]
print(array)
result = [1 for index in range(len(array)) if check_neighbours(index, array)]
print(sum(result))




# ВТОРОЕ РЕШЕНИЕ (закольцованный массив)

def both_less(sp):
    count = 0
    for i in range(len(sp)):
        if sp[i - 1] < sp[i] > sp[i - len(sp) + 1]:
            count += 1
    print(count)


n = int(input("Введите кол-во элементов массива: "))
sp = [random.randint(0, 10) for _ in range(n)]
print(sp)
# print(i for i in range(len(sp)) if (sp[i - 1] < sp[i] and sp[i] > sp[i - len(sp) + 1]))
both_less(sp)

