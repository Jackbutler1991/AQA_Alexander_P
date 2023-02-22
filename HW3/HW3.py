import random
<<<<<<< HEAD


# HW 3.1 Привести к целому типу -1.6, 2.99
def float_to_int(var_int: int) -> int:
    var_int = int(var_int)
    return var_int


# int_namber1 = int(-1.6)
# int_namber2 = int(2.99)
# print(int_namber1, int_namber2)

# WM 3.2 Заменить символ # в строке
def change_symbol_in_str(var_change: str) -> str:
    var_change = var_change.replace("#", "/")
    return var_change


# print(change_symbol_in_str('www.my_site.com#about'))

# HW 3.3 Добавить 'ing' к слову stroka
def add_ing(var_ing_add: str) -> str:
    var_ing_add = var_ing_add + 'ing'
    return var_ing_add


# print(add_ing("stroka"))

# HW 3.4 в строке Ivan Ivanov поменять слова местами
def swap(str_ivan):
    return ' '.join(str_ivan.split(' ')[::-1])


# str_ivan = swap("Ivan Ivanov")
# str_lena = swap("Lena Ivanova")

# HW 3.5 удалить пробелы вначале и вконце строки
def delete_space(var_del: str) -> str:
    var_del = var_del.strip()
    return var_del


# print(delete_space(" HELLO "))
=======
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
>>>>>>> 3b480b6d167ad48418a6afea71e448367339e8e6

# HW 3.6 создайте переменную School
school = {"1а": 23, "1б": 22, "1в": 21, "2a": 20, "2,б": 19, "2в": 20,
          "3а": 18, "4б": 24, "5а": 23, "6а": 15, }

<<<<<<< HEAD

# HW 3.7 cоздайте список и извлеките из него списка второй элемент
def make_list(hw_list: list) -> list:
    return hw_list


# hw_list = [1, 123.1, 'Petr', [1, 3.14], 'Minsk']
# print(make_list(hw_list[1]))

# HW 3.8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
def find_str(str_find: str, index: str) -> int:
    index = str_find.find(index)
    return index


# print(find_str("Houston, we have a problem" ,"problem"))
# если строка не найдена, выводит -> -1

# HW 3.9 Вывести нужные символы из фразы "My name is Agent Smith" "y" и "nesgt"
def str_out_symb(var_str: str, str_output) -> str:
    return var_str[str_output]


def str_out_str(var_str: str, str_output1, str_output2, str_output3):
    return var_str[str_output1:str_output2:str_output3]


# str_output = "My name is Agent Smith"
# print(str_out_symb(str_output, 1))
# print(str_out_str(str_output, 3, 16, 3))

# print(str_out(str_output, 1))
# print(str_output[3:16:3])

# Напишите программу, которая будет выводить уникальное число
def random_namber(var_at, var_to) -> int:
    random_namber = random.randrange(var_at, var_to)
    return random_namber

# print(random_namber(1, 100))
=======
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

>>>>>>> 3b480b6d167ad48418a6afea71e448367339e8e6
