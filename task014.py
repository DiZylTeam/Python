# Требуется вывести все целые степени двойки (т.е. числа
# вида 2 k), не превосходящие числа N.

# 10 -> 1 2 4 8


num = int(input('Enter a number: '))    # ввод пользователем числа
n = 2   # задаем переменную со значением 2 (число-основание) 
k = 0   # задаем переменную со значением 0 (степень возведения, 0 - первая степень)
while n ** k <= num:    # запускаем цикл while для сравнения результата возведения двойки в степень с введенным пользователем числом
    print(n ** k, end = "  ")   # выводим каждый результат возведения в степень (end = " " - функция для выведения значений в один ряд 
                                # через какой-либо знак препинания или пробел)
    k += 1  # после каждого прохода прибавляем +1 к степени

