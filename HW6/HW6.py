import pickle

def new_file(write_in_file) -> str:
    new_file = open("file_HW6_1.txt", "w+")
    new_file.write(write_in_file)
    new_file.close()
    return
#new_file("22432343")

# 4.1 Вывести первый, второй,
# предпоследний и последний
# элементы файла. Если чисел
# меньше 3 выводить ошибку

def read_file(read_file) -> str:
    with open(read_file) as file:
        var_int = file.read()
        if len(var_int) < 4:
            print("Error")
        else:
            var_int1 = var_int[:2]
            var_int2 = var_int[-2:]
    return      print(f"Первый и второй: {var_int1}"
                      f"\nПоследний и предпоследний: {var_int2}")


#read_file("file_HW6_1.txt")

#4.2 Дан файл целых чисел. Создать два новых файла,
# первый из которых содержит четные числа из исходного
# файла, а второй — нечетные (в том же порядке). Если
# четные или нечетные числа в исходном файле отсутствуют,
# то соответствующий результирующий файл оставить пустым.
def sort_file(read_file, file2, file3) -> str:
    num = 0
    with open(read_file, "r") as file, open(file2, "w+") as\
            file2, open(file3, "w+") as file3:
        for num in file:
            for one_numb in num:
                if int(one_numb) % 2 == 0:
                    file2.write(one_numb)
                else:
                    file3.write(one_numb)

#sort_file("file_HW6_1.txt", "file2", "file3")


# 4.3 Дан файл вещественных чисел. Заменить в нем все
# элементы на их квадраты.

def square_file(read_file) -> str:
    sqnum = []
    with open(read_file, "r+") as file:
        for num in file:
            sqnum = ([int(x) ** 2 for x in num.split()])
        file.seek(0)
        for element in sqnum:
            file.write(str(element))
            file.write(" ")


#square_file("file_HW6_3.txt")


# 4.4 Даны два файла произвольного типа. Поменять
# местами их содержимое. Файлы должны быть
# бинарного типа


# Функция для записи файла
def bin_change(file_name, input_data) -> str:
    with open(file_name, "wb") as f:
        pickle.dump(input_data, f)

# Поменять содержимое местами
def change_files(f_bin1, f_bin2) -> str:
    b1, b2 = read_bin(f_bin1, f_bin2)
    b1, b2 = b2, b1
    bin_change(f_bin1, b1)
    bin_change(f_bin2, b2)

# прочитать файл и записать в переменные
def read_bin(file_name1, file_name2) -> str:
    with open(file_name1, "rb") as f1, open(file_name2, "rb") as f2:
        b1 = pickle.load(f1)
        b2 = pickle.load(f2)
    return b1, b2

# расшифровать файлы для проверки
def decode_bin (file_name1, file_name2) -> str:
    with open(file_name1, "rb") as f1, open(file_name2, "rb") as f2:
        b1 = pickle.load(f1)
        b2 = pickle.load(f2)
        print(f"Данные в первом файле: {b1}")
        print(f"Данные во втором файле: {b2}")
    return b1, b2

#bin_change("bin1.bin", 123)
#bin_change("bin2.bin", 321)

#decode_bin("bin1.bin", "bin2.bin")

#read_bin("bin1.bin", "bin2.bin")

#change_files("bin1.bin", "bin2.bin")

#decode_bin("bin1.bin", "bin2.bin")