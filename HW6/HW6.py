def new_file(write_in_file) -> str:
    new_file = open("file_HW6_1.txt", "w+")
    new_file.write(write_in_file)
    new_file.close()
    return
new_file("22432343")

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
            print(var_int1, var_int2)
    return

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

sort_file("file_HW6_1.txt", "file2", "file3")


# 4.3 Дан файл вещественных чисел. Заменить в нем все
# элементы на их квадраты.

def square_file(read_file) -> str:
    with open(read_file, "r+") as file:
        for num in file:
            sqnum = ([int(x) ** 2 for x in num.split()])
        file.seek(0)
        file.write(str(sqnum))


square_file("file_HW6_3.txt")






