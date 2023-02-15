# Условия
# 1 Дано целое число, если оно положительное, то прибавить к нему 1, или не изменять
def pos_plus(var_int):
    if var_int > 0:
        var_int = var_int + 1
        print(var_int)
    else:
        print(var_int)
    return

pos_plus(-1)

# 2 Найти количество положительных чисел в наборе из трех
def pos_sum(var_list):
    sum = 0
    for val in var_list:
        if val > 0:
            sum = sum + 1
    print(sum)

pos_sum(var_list = (-1, 3, -4))

# 3 Найти количество дней в году по номеру года
def days_in_year(year):
    if ((0 == year % 4) and (0 != year % 100)) or (0 == year % 400):
        print("366")
    else:
        print("365")

days_in_year(1924)

# 4 Найти день недели соответствующий цифре
def what_is_day(day):
    week = {1: "s", 2: "m", 3: "t", 4: "w", 5: "t", 6: "f", 7: "s"}
    if 0 > day < 8:
        print(week[day])

what_is_day(3)

# 5 Найти день недели соответствующий цифре
def what_is_day(day):
    week = {1: "Monday", 2: "Tuesday", 3: "Wednsday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sanday"}
    if 0 < day < 8:
        print(week[day])
    else:
        print("Error")

what_is_day(2)

# 5 Перевести массу в киллограмы
def in_kg(mesure, mass):
    convert_mass = {1: 1, 2: 0.000001, 3: 0.001, 4: 1000, 5: 100}
    if 0 < mesure < 6:
        mass = mass * convert_mass[mesure]
        print(f'Масса в киллограммах: {mass}')
    else:
        print("Error")
    return

in_kg(4, 1234)
