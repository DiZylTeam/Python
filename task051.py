# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                 Вывод:
# values = [0, 2, 10, 6]                same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

#objects = [0, 2, 10, 6]



def same_by(characteristic, objects):
    n = len(list(filter(characteristic, objects)))
    print(n)
    return not n or n == len(objects)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print(True)
else:
    print(False)
