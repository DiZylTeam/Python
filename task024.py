# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


# 4 -> 1 2 3 4
# 9


import random
n = int(input("Кол-во кустов на грядке: "))
berries = []
while len(berries) < n:
    berries.append(random.randint(1, 10))
print(f"Количество ягод на кустах: {berries}")

# n_sel = int(input("Выберите куст для сбора ягод: "))

max_berries = 0

for i in berries:
    if i == 0:
        n_pre = berries[n - 1]
        n_next = berries[i + 1]
        res_berries = berries[i] + n_pre + n_next
        if res_berries > max_berries:
            max_berries = res_berries
    elif 0 < i < n - 1:
        n_pre = berries[i - 1]
        n_next = berries[i + 1]
        res_berries = berries[i] + n_pre + n_next
        if res_berries > max_berries:
            max_berries = res_berries
    elif i == n - 1:
        n_next = berries[0]
        n_pre = berries[i - 1]
        res_berries = berries[i] + n_pre + n_next
        if res_berries > max_berries:
            max_berries = res_berries

print(f"Максимльное количество собранных ягод: {max_berries}")



