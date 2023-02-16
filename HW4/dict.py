# Cловари

#1 Создайте словарь связав его с переменной School
school = {"1а": 23, "1б": 22, "1в": 21, "2a": 20, "2б": 19, "2в": 20,
          "3а": 18, "4б": 24, "5а": 23, "6а": 15, }

#2 Узнайте сколько человек в каком-нибудь классе
def school_hmp(numb_class):
    return school[numb_class]
print(school_hmp ("1а"))

#3 В школе произошли изменения.
    #3.1 Изменить количество учеников в 3 классах
def school_change(name_class, val):
    school_new = school[name_class]=val
    return school_new

school_change("1а", 230)
school_change("1б", 1273)

    #3.2 Добавить 2 класса
def school_add(name_class, val):
    school_new = school[name_class]=val
    return school_new

school_add("11a", 100)
school_add("12г", 1)

    #3.3 Удалить 1 класс
def school_del(name_class):
     del school[name_class]
     return

school_del("4б")

#4 Вывести содержимое словаря на экран
for school_class, students in school.items():
    print(f"Сlass number: {school_class}, Number of students: {students}")
