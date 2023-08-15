# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]




def find_range_numbers(min_num, max_num, array):
    sp = [item for item in range(0, len(array)) if min_num <= array[item] <= max_num]
    return sp




import random

n = int(input("Введите кол-во элементов массива: "))
array = [random.randint(0, 100) for _ in range(n)]
print(array)
min_num = int(input("Введите минимальный элемент диапазона: "))
max_num = int(input("Введите максимальный элемент диапазона: "))
print(find_range_numbers(min_num, max_num, array))
