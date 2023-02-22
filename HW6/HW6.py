def new_file(write_in_file) -> str:
    new_file = open("file_HW6_1.txt", "w+")
    new_file.write(write_in_file)
    new_file.close()
    return
new_file("12332122565")

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

#4.2
def sort_file(read_file, file2, file3) -> str:
    num = 0
    with open(read_file, "r") as file, open(file2, "w+") as file2, open(file3, "w+") as file3:
        for num in file:
            for one_numb in num:
                if int(one_numb) % 2 == 0:
                    file2.write(one_numb)
                else:
                    file3.write(one_numb)

sort_file("file_HW6_1.txt", "file2", "file3")








