# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


import random                               # импорт функции random для нашего кода
n = int(input('Enter the number of coins: '))
coin = []                                   # задаем массив (для монет)
i = 0                                       # задаем переменную i для счетчика
min1 = 0                                    # задаем переменную min1 для одной стороны монет (например, "орёл")
min2 = 0                                    # задаем переменную min2 для второй стороны монет (например, "решка")
while i < n:                                # запускаем цикл while для перебора массива
    coin.append(random.randint(0, 1))       # задаем значение массива из рандомных значений 0 ("орёл") и 1 ("решка")
    if coin[i] == 0:                        # вводим условный оператор if для подсчета количества сторон монет со значениями 0 и 1
        min1 += 1
    else:
        min2 += 1
    i += 1
print(coin) 
if min1 <= min2:                            # сравниваем полученные количества сторон и выводим минимальное из них
    print(f"Минимальное количество монет, которые необходимо перевернуть: {min1}")
else:
    print(f"Минимальное количество монет, которые необходимо перевернуть: {min2}")