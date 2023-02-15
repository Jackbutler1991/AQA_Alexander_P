# Преобразование типов

# 1 Перевести строку в массив
def change_str_to_arrays(var_str):
    return var_str.split(" ")


print(change_str_to_arrays("Robin Singh"))
print(change_str_to_arrays("I love arrays they are my favorite"))

# 2 Дан список. Напечатать текст
var_list = ["Ivan", "Ivanow"]
var_str_city = "Minsk"
var_str_country = "Belarus"

print(f"Привет {' '.join(var_list)}! Добро пожаловать в {var_str_city} {var_str_country}")

# 3 Дан список. Сделать из него строку
var_list_st = ["I", "love", "arrays", "they", "are", "my", "favorite"]
var_str_st = var_list_st.split(" ")
