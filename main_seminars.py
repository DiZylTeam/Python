# sp = []
# sp.append(65465)
# sp.append("privet")
# sp.append(4.5)
# sp.append([5, 7])
# sp.append(True)
# print(sp)


# i = 0
# while i<10:
#     print(i, end = " ; ")
#     i += 1

# for _ in range(4):
#     print("hello")


# for i in sp:
#     print(i)

# for i in range(5, 15, 3):
#     print(i)



# sp = []
# sp.append(5)
# sp.extend([7, 8, True])
# sp.insert(0, 5.7)
# sp = sp + [1, 2]
# print(sp)
# print(sp[3::])
# print(sp[2:5])
# print(sp[-5])

# a = sp.pop()
# print(a)
# sp.remove(True)
# del sp[0]

# for i, k in enumerate(sp):
#     print(i, k)
# print(sp)# проверка встроенной функцией bin



# t = (4, 8, 9)
# print(t)
# print(t[0])


# d = {}
# d["uncle Bance"] = "+79269554300"
# d["aunt Helen"] = "+79548659745"
# del d["uncle Bance"]
# print(d)

# for key, value in d.items():
#     print(key, value)

# print(d.keys())
# print(d.values())



# s = set()   # множество
# s.add(5)
# s.add(7)
# print(s)
# print(5 in s)

# list tuple dict set


# Анотация типов и профилирование

# x: int = 5      # типизация переменных - указываем их тип (появилось в версии Python 3.5)
# y: int = 3      # удобно для больших проектов
# print(x + y)


# x: int = "Hello"    # также будет работать корректно, т.к. выполняется инконтенация, не смотря на то, что анотация типов нарушается
# y: int = " world!"  # т.е. в данном случае также работает динамическая типизация Python
# print(x + y)


# def summa(x1, x2):       # создание локальных функций (методов): def + название функции + переменные на вход в '()'
#     print(x1 + x2)      # можно выводить результат без возврата с помощью return

# summa(8, 12)            # вызов функции с передачей ей значений. Будет выводится результат на консоль без print, т.к. он есть в самой функции



# def summa2(x1: int, x2: int):   # с типизацией переменных
#     res: int = x1 + x2
#     return res                  # возвращаем результат с помощью return

# print(summa2(7, 13))            # при return - выводить на консоль с помощью print
# print(summa2("Hello", " world!"))   # также будет работать корректно, т.к. выполняется инконтенация, не смотря на то, что анотация типов нарушается



# N = int(input("Введите натуральное число "))

# summa = 0
# while True:
#     summa = summa + N
#     N = N - 1
#     if N == 0:
#         break
# print(summa)


# def Summ(N):
#     summa = 0
#     while True:
#         summa = summa + N
#         N = N - 1
#         if N == 0:
#             break
#     return summa

# N = int(input("Введите натуральное число "))
# print(Summ(N))




# def Summ_rec(N):
#     if N == 1:
#         return 1
#     return N + Summ_rec(N-1)

# # N = int(input("Введите натуральное число "))
# print(Summ_rec(4))


# from random import randint

# def square(sp):
#     result = []
#     for item in sp:
#         result.append(item**2)
#     return result




# print(square(sp))
# print([item**2 for item in sp])

# print([randint(0, 10) for _ in range(10)])




# def find4_and_square(sp):
#     result = []
#     for item in sp:
#         if item > 4:
#             result.append(item**2)
#     return result




# sp = [1, 5, 3, 8, 10, 2]

# print(find4_and_square(sp))
# print([item**2 for item in sp if item > 4])
# print(5 in sp)
# print(5 not in sp)


# ===== ФУНКЦИИ ВЫСШЕГО ПОРЯДКА =====

# def create_phrase(func, word):
#     print(func(word))


# def hello(s):
#     return f"Hello {s}"

# def bye(s):
#     return f"{s} bye-bye"

# create_phrase(hello, "world!")
# create_phrase(hello, "Dmitry!")
# create_phrase(bye, "world")
# create_phrase(bye, "Dmitry")



# def calc_power(degree):
#     def power(number):
#         return number ** degree
#     return power

# print(calc_power(2)(3))
# square = calc_power(2)
# cube = calc_power(3)

# print(square(2))
# print(cube(3))


# print((lambda x, y: x+y) (5, 8))

# calc = {"+": lambda x, y: x+y,
#         "-": lambda x, y: x-y,
#         "*": lambda x, y: x*y,
#         "/": lambda x, y: x/y
#         }

# print(calc["+"](5, 15))
# print(calc["+"](5, 300))


sp = [5, 8, 1, 11, 3, 2]
print(*map(lambda item: item**2, sp))
print(list(map(lambda item: item**2, sp)))
print(list(map(lambda item: item**2 if item > 5 else 0, sp)))
print(*filter(lambda item: True if item > 5 else False, sp))
print(list(filter(lambda item: True if item > 5 else False, sp)))
print(*sp)

for i, v in enumerate(sp):
    print(i, v)




names = ["Петя", "Ваня"]
sp = [5, 8, 1, 11, 3, 2]

for x1, x2 in zip(names, sp):
    print(x1, x2)
