
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:       Вывод:
# 1 2 3 2 3   2


import random

def find_pairs(sp):
    summ = 0
    for i in set(sp):
        # print(i, sp.count(i))
        summ += sp.count(i) // 2
    print(summ)



n = int(input("Введите кол-во элементов массива: "))
sp = [random.randint(0, 5) for _ in range(n)]
print(sp)
print(set(sp))
find_pairs(sp)
# print(sum([sp.count(i)//2 for i in set(sp)]))     # решение в одну строку

