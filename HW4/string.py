#Строки

#1) 
var_str = "homeless" #8 символов
var_str1 = var_str[1:7] #удаляем первый и последний
var_str2 = var_str[0:2] + var_str[2+1:] #удаляемтретий с начала
var_str3 = var_str[0:-3] + var_str[-3+1:] #удаляем третий с конца
print ("Без первого и последнего символа:",var_str1)
print ("Без третьего символа:", var_str2)
print ("Без третьего символа с конца:", var_str3)
print ("Количество символов в строке:", len(var_str))

#2)
var_str15 = "quizzifications"
var_str15_1 = var_str15[7:] #удаляем первые 8 символов
var_str15_2 = var_str15[0:5] + var_str15[9:] #удаляем символы из середины
var_str15_3 = var_str15[0:2] + var_str15[3:5] + var_str15[6:8] + var_str15[9:11] + var_str15[12:14] #удаляем индексы кратные 3
var_str15_4 = var_str15[::-1]

print(var_str15_1)
print(var_str15_2)
print(var_str15_3)
print(var_str15_4)

#3)
var_name = "my name is name"
var_list = var_name.split(' ')
var_list.pop(3)
print(' '.join(var_list), "Alexander")

#4)
test_tring = "Hello world!"
test_tring_w = test_tring.find("w")
test_tring_l = test_tring.count("l") 
test_tring_start = test_tring.startswith("Hello")
test_tring_end = test_tring.endswith("qwe")


print(test_tring_w)
print(test_tring_l)
print(test_tring_start)
print(test_tring_end)