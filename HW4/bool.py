# Логические операции

#1 Присвоить двум переменным любые числовые значения
var_a, var_b = 1, 2

#2 Составить 4 логических выражения с AND
var_a < var_b and var_a < 3 #True
var_c = var_a == 1 and var_b == 2 #True

var_a > var_b and var_a < 3 #False
var_a * 5 == 12 and var_b == 2 #False

#3 Составить 4 логических выражения с OR
var_a * 5 == 12 or var_b == 2 #True
var_a / 1 + 10 == 11 or var_b * 2 == 5 #True

var_a > var_b or var_a > 3 #False
var_a + 3 == 7 or var_b ** 2 == 15 #False

#4 Составить логическое выражение со строкой
var_str = 'apple pie'
var_c = var_str == 'apple pie' and var_a < 6 and (var_b == 1 or var_a == 1) #True
print(var_c)