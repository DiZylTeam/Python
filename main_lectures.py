# a = 5
# b = 5.89
# c = 'hello'

# print(a, b, c)  # для вывода нескольких переменных - указываем их через запятые

# print(a, '-', b, '-', c)    # для вывода переменных через какие-либо знаки препинания - эти знаки помещаем в кавычки

# print(f"{a} - {b} - {c}")   # вывод на консоль методом интерполяции

# print("{} - {} - {}".format(a,b,c)) # можно выводить через формат .format




# # ===== ВВОД ДАННЫХ =====


# print('Enter the first number: ')
# a = input()   # с помощью функции input можем ввести каки-либо данные, но они будут сохраняться в виде строки str
# # при вышеуказанном способе ввода данных - данные вводятся с новой строки
# b = input('Enter the second number: ')  # второй метод для ввода данных - введение будет на той же строке

# print(a, '+', b, '=', a + b)  # в данном случае не будет сложение чисел, а будет склеивание чисел, т.к. числа введены как тип str


# print('Enter the first number: ')
# a = int(input())    # указываем тип данных int, чтобы на ввод программа видела значение, как число, а не как строку
# b = int(input('Enter the second number: '))

# print(a, '+', b, '=', a + b)    # в данном случае будет сложение чисел, т.к. в значениях переменных указали тип int





# # ===== ПЕРЕВОД ЗНАЧЕНИЙ ИЗ ОДНОГО ТИПА ДАННЫХ В ДРУГОЙ =====

# c = 5.89    # вещественное число типа float
# print(c)
# print(type(c))

# c = int(c)  # меняем тип данных переменной "с" на int
# print(c)
# print(type(c))

# c = str(c)  # меняем тип данных переменной "с" на str
# print(c)
# print(type(c))

# # НО!!! Нельзя перевести строку str с буквами в int
# v = 'hello'
# v = int(v)
# print(v)

# c = 1    # вещественное число типа float
# print(c)
# print(type(c))

# c = bool(c)  # меняем тип данных переменной "с" на bool
# print(c)
# print(type(c))


# ===== АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ =====

# a = 5.59786
# b = 6.558432
# print(a*b)

# print(round(a*b, 3))    # функция round округляет вещественные числа до нужных значений
# # указываем число или действие с переменными, после запятой указываем количество чисел, которые надо вывести




# ===== IF - ELSE ======

# username = input('Enter a name: ')
# if username == "Mariya":
#     print("Wow, this is Mariya!")
# elif username == "Dmitry":
#     print("We wait you Dmitry!")
# else:
#     print('Hello, ', username + '!')



# ===== ЦИКЛ WHILE ======

# i = 0
# while i < 5:
#   if i == 3:
#       break
#       i = i + 1
#   else:
#       print('Пожалуй')
#       print('OK')
# print(i)


# ===== ЦИКЛ FOR ======

# a = 'qwerty'
# print(a[2]) # вывод нужного элемента в строке (как в массиве, нумерация элементов такая же - начинается с нуля)

# for i in a:
#     print(i)    # вывод каждого элемента переменной с помощью цикла for


# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)


# # ===== Команды для работы со строками: =====


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# # 1. Определить количество символов в строке:
# print(len(text)) # 39
# # 2. Проверить наличие символа в строке (in):
# print('ещё' in text) # True
# # 3. Функция, которая делает все буквы строки маленькими:
# print(text.lower()) # съешь ещё этих мягких французских булок
# # 4. Функция, которая делает все буквы строки большими:
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# # 5. Заменить слово на другое :
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок


# ===== СРЕЗЫ =====

# ● Мы представляем строку в виде массива символов. Значит мы можем
# обращаться к элементам по индексам.
# ● Отрицательное число в индексе — счёт с конца строки

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...



# git remote add origin https://github.com/DiZylTeam/Python.git
# git branch -M main
# git push -u origin main




# def f(x):
#     return x*x


# a = f

# print(f(5))
# print(a(5))




# def calk1(a):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):    # в функцию 'math' передаем ссылку на функции calk1 или calk2 -> переменная 'op' имеет ссылку на эти функции 
#     print(op(x))    # вызываем функцию на экран


# math(calk2, 5)




# def calk1(a, b):    # с двумя аргументами
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):    # с двумя аргументами 
#     print(op(x, y))


# math(calk2, 5, 10)      # обозначаем два аргумента







# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))


# calk1 = lambda a, b: a + b  # лямбда-функция для сокращения локальных функций

# math(calk1, 5, 10)
# math(lambda a, b: a + b, 5, 10) # можно лямбда-функцию сразу вставлять на вывод




# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]



# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# sp2 = []
# for i in sp:
#     if i % 2 == 0:
#         sp2.append((i, i*i))
# print(sp2)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]


# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# sp2 = select(int, sp)
# print(sp2)
# sp2 = where(lambda x: x % 2 == 0, sp2)
# print(sp2)
# sp2 = list(select(lambda x: (x, x**2), sp2))
# print(sp2)





# ===== Функция map =====

# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.


list_1 = [x for x in range (1, 20)]
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)



# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?


# 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем список из
# значений строки, пример:

data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

# 2. Теперь вернемся к задаче. С помощью функции map():

data = list(map(int,input().split()))


# ==== Функция filter ====

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.


data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]


# Как в данном случае работает функция filter()? Все данные, которые находятся внутри проходят
# через функцию, которая указана следующим образом:
# lambda x: x % 2 == 0
# То есть делает проверка на те числа, которые при делении на 2 дают в остатке 0. Тем самым мы
# ищем только четные числа. Действительно преобразовав наши итоговые данные в список, с
# помощью функции list(), мы с Вами можем наблюдать такой красивый результат 



# ==== Функция zip ====

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# из элементов входных данных
# На выходе получаем набор данных, состоящий из элементов соответствующих
# исходному набору.


users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip () пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]




# ==== Функция enumerate ====

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.
# Функция enumerate() позволяет пронумеровать набор данных.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users)
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]



# ===== Файлы =====

# Варианты режима (мод):
# a – открытие для добавления данных.
#   ○ Позволяет дописывать что-то в имеющийся файл.
#   ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
# и в него начнется запись.

# r – открытие для чтения данных.
#   ○ Позволяет читать данные из файла.
#   ○ Если вы попробуете считать данные из файла, которого не существует, программа
# выдаст ошибку.

# w – открытие для записи данных.
#   ○ Позволяет записывать данные и создавать файл, если его не существует.

# Миксованные режимы:
# 1. w+
#   ○ Позволяет открывать файл для записи и читать из него.
#   ○ Если файла не существует, он будет создан.
# 2. r+
#   ○ Позволяет открывать файл для чтения и дописывать в него.
#   ○ Если файла не существует, программа выдаст ошибку.



# Примеры использования различных режимов в коде:
# 1. Режим a
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
    data.writelines(colors) # разделителей не будет
    data.close()

# ● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой
# переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redgreenblue.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в
# существующий файл, а не перезапись файлов.

# Ещё один способ записи данных в файл:
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# 2. Режим r
# ● Чтение данных из файла:
path = 'file.txt'
data = open(path, 'r')
for line in data:
print(line)

# 3. Режим w
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.




