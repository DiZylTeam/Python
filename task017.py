# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


sp = [1, 1, 2, 0, -1, 3, 4, 4]
sp_2 = []
for i in sp:
    if i not in sp_2:
        sp_2.append(i)
print(len(sp_2))

