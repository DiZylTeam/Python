# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1




def remove_marks(num, i = 0):
    if i == len(num):
        return num
    if num[i] > 3:
        num[i] = 1
    remove_marks(num, i + 1)




import random
n = int(input('Количество оценок: '))
marks = []
for i in range(n):
    marks.append(random.randint(1, 5))
print(marks)

remove_marks(marks)
print(marks)


