# *** Список (list) ***

# Создание пустого списка

my_list = []
my_list_2 = list()

# добавление объекта (в конец списка)
my_list.append(100)
my_list.append(77)
my_list.append("A")
my_list.append([1,23,4])

# обращение к элементам списка
# замена значний
my_list[0] = 5
my_list[-2] = "B"

# чтение значений
element_value = my_list[1]

#удаление значений
# del my_list[-1]

# my_list.remove(5)

# a = my_list.pop(0)

# создание заполненного списка

my_list_2 = [10, 20, 30, 'A', "hello", True, 3.14, [1,2,3]]

# "длина" списка - количество элементов
# print(len(my_list_2))

# создание списка из строки
s = "Привет, Мир!"
ListFromStr = list(s)

# print(ListFromStr)

# методы списка

# исходный список
x = [1,2,3,4,5]

# представление
y = x

# y[2] = 100

# копия
z = x.copy()

z[2] = 100

print(f"x: {x}; z: {z}")