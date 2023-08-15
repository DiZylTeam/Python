# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes







def simple_number(number, n):
    if number <= 1:
        return True
    elif n % number == 0:
        return False
    return simple_number(number - 1, n)




n = int(input("Введите число: "))
number = n
print(simple_number(n - 1, n))




# def simple_number(number, input_num):
#     if number <= 1:
#         return True
#     elif input_num % number == 0:
#         return False

#     return simple_number(number - 1, input_num)

# print(simple_number(num - 1, num))

