# Циклы
# 1 Найти сумму всех целых чисел от А до В включительно
def var_sum(var_int_a, var_int_b):
    all_sum = 0
    for int_sum in range(var_int_a, var_int_b + 1):
        all_sum = all_sum + int_sum
    return all_sum


#print(var_sum(2, 4))


# 3 Найти произведение положительных, сумму и колличество отрицательных значений
def sum_sab_numbers(numbers):
    count, num_sub, num_pos = 0, 0, 1
    for item in numbers:
        if item < 0:
            num_sub = num_sub + item
            count = count + 1
        else:
            num_pos = num_pos * item
    return count, num_sub, num_pos


#numbers = [1, -1, 2, -2, 3, 4, 5, -6, -9, 1]
#print(sum_sab_numbers(numbers))


# 4 Дан словарь пловцов с их результатами. Напечатать лучший результат среди 6 участников


def winner(competitors):
    winner_list = []
    for item in competitors:
        winner_list.append(competitors[item])
    return max(winner_list)


#competitors = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12,
              # "Давидович Татьяна": 30, "Дешук Дмитрий": 24.01, "Казак Анна": 28.17}

#print(winner(competitors))


# 5 Вывести уникальное число из массива


def uniq(numbers_list):
    for item in numbers_list:
        if numbers_list.count(item) < 2:
            return item


#numbers_list = [1, 5, 2, 9, 2, 9, 1]
#print(uniq(numbers_list))
