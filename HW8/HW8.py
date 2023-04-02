# 1 Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:

def decorator(funk):
    def inner(type, *args):
        if type == "str":
            print('start decorator "Abb two symbols":')
            global one_symbol, two_symbol
            one_symbol, two_symbol = str(args[0]), str(args[1])
            funk(type, *args)
            print('finish decorator "Abb two symbols"')

        elif type == 'int':
            print('start decorator "Abb three numbers":')
            global one_number, two_number, three_number
            one_number, two_number, three_number = float(args[0]), \
                float(args[1]), float(args[2])
            funk(type, *args)
            print('finish decorator "Abb three numbers"')

    return inner


@decorator
def add_two_symbols(type="str", *args):
    #    print('hello world', type, a , b)
    return print(one_symbol + two_symbol)


@decorator
def add_three_symbols(type, *args):
    #    print('hello world', type, a , b)
    return print(one_number + two_number + three_number)


add_two_symbols('str', "3", 5)
add_two_symbols('str', 5, 5)
add_two_symbols('str', "a", "b")

add_three_symbols("int", 5, 6, 7)
add_three_symbols("int", "3", 5, 0)
add_three_symbols("int", 0.1, 0.2, 0.4)

# 2  На вход подаётся некоторое количествразделенных пробелом чисел...

number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen'}


def numbers(func):
    def wrapper(numbers_list):
        numbers = numbers_list.split()
        name = [number_names[int(n)] for n in numbers]
        sorted_var = sorted(name)
        sorted_var = [str(list(number_names.keys())
                          [list(number_names.values()).index(i)])
                      for i in sorted_var]

        return func(" ".join(sorted_var))

    return wrapper

@numbers
def numbers_name(numbers_list):
    return (f'sorted_numbers: {numbers_list}')

print(numbers_name("1 2 3"))