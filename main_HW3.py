from HW3 import *

# HW 3.1 Привести к целому типу -1.6, 2.99
print(float_to_int(-1.6))
print(float_to_int(2.99))

# WM 3.2 Заменить символ # в строке
print(change_symbol_in_str('www.my_site.com#about'))

# HW 3.3 Добавить 'ing' к слову stroka
print(add_ing("stroka"))

# HW 3.4 в строке Ivan Ivanov поменять слова местами
print(swap("Ivan Ivanov"))
print(swap("Lena Ivanova"))

# HW 3.5 удалить пробелы вначале и вконце строки
print(delete_space("    HELLO   "))

# HW 3.7 cоздайте список и извлеките из него списка второй элемент
hw_list = [1, 123.1, 'Petr', [1, 3.14], 'Minsk']
print(make_list(hw_list[2]))

# HW 3.8 Вывести входит ли строка1 в строку2 (пример: employ и employment)
# если строка не найдена, выводит -> -1
print(find_str("Houston, we have a problem", "problem"))

# HW 3.9 Вывести нужные символы из фразы "My name is Agent Smith" "y" и "nesgt"
str_output = "My name is Agent Smith"
print(str_out_symb(str_output, 1))
print(str_out_str(str_output, 3, 16, 3))

# Напишите программу, которая будет выводить уникальное число
print(random_namber(1, 100000))
