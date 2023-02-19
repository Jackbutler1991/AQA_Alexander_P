# Преобразование типов

# 1 Перевести строку в массив
def change_str_to_arrays(var_str):
    return var_str.split(" ")


#print(change_str_to_arrays("Robin Singh"))
#print(change_str_to_arrays("I love arrays they are my favorite"))

# 2 Дан список. Напечатать текст
var_list = ["Ivan", "Ivanow"]
var_str_city = "Minsk"
var_str_country = "Belarus"

def print_text(var_list: list, var_str_city: str, var_str_country: str):
    print_text = f"Привет {' '.join(var_list)}! Добро пожаловать в {var_str_city} {var_str_country}"
    return print_text

#print(f"Привет {' '.join(var_list)}! Добро пожаловать в {var_str_city} {var_str_country}")

# 3 Дан список. Сделать из него строку

def change_list_to_str(var_list):
    change_list_to_str = " ".join(var_list)
    return change_list_to_str

#var_list_st = ["I", "love", "arrays", "they", "are", "my", "favorite"]
#print(" ".join(var_list_st))


# 4 Создать список из 10 элементов, вставить на 3-ю позицию новое значение, удалить 6-тое
def correct_list_ten_elements(var_list, var_index_change, var_change, var_del) -> int:
    var_list.insert(var_index_change, var_change)
    var_list.pop(var_del)
    return var_list


#var_list10 = [1, 2, 3, 15, 56, 31, 7, 8, 2344556, 1]
#print(correct_list_ten_elements(var_list10, 2, 1000, 5))


# 5 Есть два словаря. Обьеденить их по ключам

def dict_union(dict_a, dict_b, dict_ab) -> dict:
    for key, value in dict_a.items():
        if key in dict_b:
            dict_ab[key] = [dict_a[key], dict_b[key]]
        else:
            dict_ab[key] = [value, None]

    for key, value in dict_b.items():
        if key in dict_a:
            dict_ab[key] = [dict_a[key], dict_b[key]]
        else:
            dict_ab[key] = [None, value]
    return dict_ab


#a = {"a": 1, "b": 2, "c": 3}
#b = {"c": 3, "d": 4, "e": 5}
#ab = {}
#print(dict_union(a, b, ab))
