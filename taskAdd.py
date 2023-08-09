
# age = int(input('Сколько вам полных лет: '))
# salary = int(input('Ваша среднемесячная зарплата: '))
# sum = int(input('Сумма кредита: '))
# period = int(input('Срок кредита (в месяцах): '))
# monthpayment = sum / period

# if monthpayment > salary / 2:
#     print('Кредит не одобрен!')
# elif (age * 12) + (period / 12) > 600:
#     print('Кредит не одобрен!')
# else:
#     print('Кредит одобрен!')



# Дан некоторый список чисел. Задача - найти сколько раз встречается введенная пользователем ЦИФРА в данных числах


# sp = [1, 55, 15, 7, 85, 0, 99]
# print(sp)
# digit = int(input('Enter a digit from 0 to 9: '))
# count = 0
# sp_2 = []

# for i in sp:
#     if i % 10 == 0:
#         sp_2.append(i)
#     else:
#         i = i % 10
#         sp_2.append(i)
#         i // 10



# print(count)





# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать как многочлен степени k.

# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите натуральную максимальную степень "))
sp = [randint(0,10) for _ in range(k+1)]
print(sp)

#[0,8,1,10] - > 8*x^2 + x +10 = 0



