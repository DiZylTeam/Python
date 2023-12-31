# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15



def arithmetic_progression(a1, d, n):
    for _ in range(n):
        sp.append(a1 + (n - 1) * d)
        n = n - 1
    return sp




a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность (шаг) арифметической прогрессии: "))
n = int(input("Введите кол-во элементов арифметической прогрессии: "))
sp = []
sp = arithmetic_progression(a1, d, n)
sp.sort()
print(sp)

