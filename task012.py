# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3



sum = int(input('Enter the sum of numbers: '))      # ввод суммы чисел
mult = int(input('Enter the multiplication of numbers: '))  # ввод произведения чисел
num_1 = 0                   # первое загаданное число (присваиваем значение 0)
num_2 = 0                   # второе загаданное число (присваиваем значение 0)
while num_1 <= 1000:        # запускаем цикл while для переборки в переменной num_1 чисел до 1000 (согласно условиям задачи)
    num_2 = num_1           # присваиваем переменной num_2 значение переменной num_1, чтобы после каждого прохода цикла не выполнялись 
                            # одни и те же операции с такими же числами, только в обратном порядке (как в таюлице умножения), иначе на консоль 
                            # нужные числа будут выводится два раза, в обратном порядке)
    while num_2 <= 1000:    # запускаем еще один цикл while для переборки в переменной num_2 чисел до 1000 (согласно условиям задачи)
        if num_1 + num_2 == sum and num_1 * num_2 == mult:  # задаем условие для нахождения чисел (чтобы сумма num_1 и num_2 = sum И произведение num_1 и num_2 = mult)
            print(num_1, num_2)     # при выполнении условия выводим числа на консоль
        num_2 += 1                  # если условие не выполняется добавляем к num_2 +1
    num_1 += 1                      # после прохождения второго цикла while для переменной num_2 добавляем к переменной num_1 +1




