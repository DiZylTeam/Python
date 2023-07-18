# Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


num = int(input('Enter a three-digit number: '))
if num > 999 or num < 100:
    print('Invalid value!')
else:
    print((num % 10) + (num // 10) % 10 + (num // 100))





