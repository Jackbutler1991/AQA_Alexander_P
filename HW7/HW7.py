# 7.1 Lambda: Создать lambda функцию, которая принимает на вход
# имя и выводит его в формате “Hello, {name}”

f1 = lambda name: print(f"Hello {name}")

# 7.2 Lambda: Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список

f2 = lambda x: print([f"Hello, {i}" for i in x])


# 7.1 Генераторы: Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами с обработкой исключений

def gen(arr) -> list:
    return [i for i in arr if i > 0]


# 7.2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

def sum_letters(sentence):
    set = []

    def sent(var_sent):
        var_sent = var_sent.split(" ")
        for i in var_sent:
            if i == "the":
                continue
            yield len(i)

    for i in sent(sentence):
        set.append(i)
    print(set)
