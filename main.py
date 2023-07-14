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
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('OK')
# print(i)


# ===== ЦИКЛ FOR ======

# a = 'qwerty'
# print(a[2]) # вывод нужного элемента в строке (как в массиве, нумерация элементов такая же - начинается с нуля)

# for i in a:
#     print(i)    # вывод каждого элемента переменной с помощью цикла for


line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)


# ===== Команды для работы со строками: =====


text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# 1. Определить количество символов в строке:
print(len(text)) # 39
# 2. Проверить наличие символа в строке (in):
print('ещё' in text) # True
# 3. Функция, которая делает все буквы строки маленькими:
print(text.lower()) # съешь ещё этих мягких французских булок
# 4. Функция, которая делает все буквы строки большими:
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# 5. Заменить слово на другое :
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок


# ===== СРЕЗЫ =====

# ● Мы представляем строку в виде массива символов. Значит мы можем
# обращаться к элементам по индексам.
# ● Отрицательное число в индексе — счёт с конца строки

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...



# git remote add origin https://github.com/DiZylTeam/Python.git
# >> git branch -M main
# >> git push -u origin main