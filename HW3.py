import random

# Задание 1.2
a = 1
a1 = 1.1
b = 'asd'
lst = [1, 2, 3, 4]
d = {'dasfd': 1, 'ghjk': 2}
bo = True
set_1 = (1, 2, 3)
print(type(a))
print(type(a1))
print(type(b))
print(type(lst))
print(type(d))
print(type(bool))
print(type(set_1))

# Задание 1.3 Найти значение выражений
x = 17/2 * 3 + 2
print (x)
x = 2 + 17 / 2 * 3
print (x)
x = 19 % 4 + 15 / 2 * 3
print (x)
x = (15 + 6) - 10 * 4
print (x)
x = 17 / 2 % 2 * 3 ** 3
print (x)

# Задание 1.4 Создать три переменные, содержащие возраст трех...
neigh1, neigh2, neigh3 = 19, 23,  39
sum_old = neigh1+ neigh2 + neigh3
print(sum_old)
avr_old = (neigh1 + neigh2 + neigh3) / 3
print(avr_old)

# HW 3.1 Привести к целому типу -1.6, 2.99
int_namber1 = int(-1.6)
int_namber2 = int(2.99)
print(int_namber1, int_namber2)

# WM 3.2 Заменить символ # в строке
a = 'www.my_site.com#about'
a = a.replace("#", "/")
print(a)

# HW 3.3 Добавить 'ing' к слову stroka
a = "stroka"
a = "stroka" + 'ing'
print(a)

# HW 3.4 в строке Ivan Ivanov поменять слова местами
str_ivan = "Ivan Ivanov"
s = ' '.join(str_ivan.split(' ')[::-1])
print(s)

# HW 3.5 удалить пробелы вначале и вконце строки
b = " HELLO "
b = a.strip()
print(b)

# HW 3.6 создайте переменную School
school = {"1а": 23, "1б": 22, "1в": 21, "2a": 20, "2,б": 19, "2в": 20, "3а": 18, "4б": 24, "5а": 23, "6а": 15, }

# HW 3.7 cоздайте список и извлеките из него списка второй элемент
hw_list = [1, 123.1, 'Petr', [1, 3.14], 'Minsk']
print(hw_list[3])

# HW 3.8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
str_find = "Houston, we have a problem"
index = str_find.find("problem")
print(index)  # если строка не найдена, выводит -> -1

# HW 3.9 Вывести нужные символы из фразы "My name is Agent Smith" "y" и "nesgt"
str_output = "My name is Agent Smith"
print(str_output[1])
print(str_output[3:16:3])

# Напишите программу, которая будет выводить уникальное число
print(random.randrange(1, 100))  # выводит случайное число в промежутке от 1 до 100