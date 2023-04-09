# Цикл While

# 1 Найти произведение всех чисел от 0 до переменной N
def mult(int_n):
    if type(int_n) not in [int]:
        raise ValueError("N not a integer type")
    elif int_n < 0:
        raise ValueError("Error N<0")
    i, a = 1, 1
    while i < (int_n + 1):
        a = i * a
        i += 1
    return a


# print(mult(6))


# 2 Поле с двумя сортами цветов S1 и S2
def sq_flow(flower_s1, flower_s2):
    if type(flower_s1 or flower_s2) not in [int]:
        raise ValueError("N not a integer type")
    elif (flower_s1 == 0 and flower_s2 == 0):
        raise ValueError("Incorrectly values")
    i = 1
    while (flower_s2 / 10) <= flower_s1:
        flower_s1 *= 2
        flower_s2 *= 3
        i += 1
    return i
sq_flow(0, 1)

# print(sq_flow(100, 3))


# 3 Дано число N. Найти колличество и сумму его цифр
def sum_numd(var_int):
    i = 0
    sum = 0
    while var_int % 10 != 0:
        sum = sum + var_int % 10
        var_int = int(var_int / 10)
        i += 1
    return sum, i


# print(sum_numd(1612))


# 4 Деду M лет, внуку N. Через сколько дед станет вдвое старше внука

def grand_old(m, n):
    i = 0
    old_m = 0
    old_n = 0
    while (m / 2) != n:
        m += 1
        n += 1
        i += 1
    return m, n, i

# print(grand_old(60, 10))
