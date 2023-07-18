
age = int(input('Сколько вам полных лет: '))
salary = int(input('Ваша среднемесячная зарплата: '))
sum = int(input('Сумма кредита: '))
period = int(input('Срок кредита (в месяцах): '))
monthpayment = sum / period

if monthpayment > salary / 2:
    print('Кредит не одобрен!')
elif (age * 12) + (period / 12) > 600:
    print('Кредит не одобрен!')
else:
    print('Кредит одобрен!')



