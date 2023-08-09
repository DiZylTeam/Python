
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

x: int = 5      # типизация переменных - указываем их тип (появилось в версии Python 3.5)
y: int = 3      # удобно для больших проектов
print(x + y)


x: int = "Hello"    # также будет работать корректно, т.к. выполняется инконтенация, не смотря на то, что анотация типов нарушается
y: int = " world!"  # т.е. в данном случае также работает динамическая типизация Python
print(x + y)


def summa(x1, x2):       # создание локальных функций (методов): def + название функции + переменные на вход в '()'
    print(x1 + x2)      # можно выводить результат без возврата с помощью return

summa(8, 12)            # вызов функции с передачей ей значений. Будет выводится результат на консоль без print, т.к. он есть в самой функции



def summa2(x1: int, x2: int):   # с типизацией переменных
    res: int = x1 + x2
    return res                  # возвращаем результат с помощью return

print(summa2(7, 13))            # при return - выводить на консоль с помощью print
print(summa2("Hello", " world!"))   # также будет работать корректно, т.к. выполняется инконтенация, не смотря на то, что анотация типов нарушается


