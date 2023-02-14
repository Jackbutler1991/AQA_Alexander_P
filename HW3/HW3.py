import random
from __init__ import swap

# HW 3.1 Привести к целому типу -1.6, 2.99
int_namber1 = int(-1.6)
int_namber2 = int(2.99)
print(int_namber1, int_namber2)

# WM 3.2 Заменить символ # в строке
var_change = 'www.my_site.com#about'
var_change = var_change.replace("#", "/")
print(var_change)

# HW 3.3 Добавить 'ing' к слову stroka
var_ing_add = "stroka"
var_ing_add = "stroka" + 'ing'
print(var_ing_add)

# HW 3.4 в строке Ivan Ivanov поменять слова местами

str_ivan = swap("Ivan Ivanov")
str_lena = swap("Lena Ivanova")

print(str_ivan)
print(str_lena)

# HW 3.5 удалить пробелы вначале и вконце строки
var_del = " HELLO "
var_del = var_del.strip()
print(var_del)

# HW 3.6 создайте переменную School
school = {"1а": 23, "1б": 22, "1в": 21, "2a": 20, "2,б": 19, "2в": 20,
          "3а": 18, "4б": 24, "5а": 23, "6а": 15, }

# HW 3.7 cоздайте список и извлеките из него списка второй элемент
hw_list = [1, 123.1, 'Petr', [1, 3.14], 'Minsk']
print(hw_list[1])

# HW 3.8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
str_find = "Houston, we have a problem"
index = str_find.find("problem")
print(index)  # если строка не найдена, выводит -> -1

# HW 3.9 Вывести нужные символы из фразы "My name is Agent Smith" "y" и "nesgt"
str_output = "My name is Agent Smith"
print(str_output[1])
print(str_output[3:16:3])

# Напишите программу, которая будет выводить уникальное число
print(random.randrange(1, 100))  # случайное число в промежутке от 1 до 100

