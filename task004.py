# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?


# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# Условия задачи:
# Петя = x
# Сережа = x
# Катя = (x + x) * 2 = 2x * 2 = 4x
# Общее количество: sum = (х + х) + 4х = 2х + 4х = 6х
# Соответственно: х = sum / 6

total_value = int(input('Enter the total number of cranes: '))
petya = total_value // 6
sergey = petya
kate = petya * 4
if total_value % 6 != 0 or total_value <= 0:
    print("They couldn't make so quantity of cranes according to the task conditions")
else:
    print(f"Petya made {petya} cranes")
    print(f"Kate made {kate} cranes")
    print(f"Sergey made {sergey} cranes")



