# *** логические операторы НЕ (NOT), И (AND), ИЛИ (OR) ***

x = True
y = False

# оператор НЕ
# print(not x)

# оператор И - возвращает True только если значения обеих 
# переменных равны True 
res = x and y

# res = False and False

# оператор ИЛИ - возвращает False только если значения обеих 
# переменных равны False
res = False or False

# print(res)


# *** Условные операторы ***

# if False:
# 	c = "Hello!"
# 	print(c)

a = -1

# if a > 0:
# 	print("больше 0")
# elif a == 0:
# 	print("равно 0")
# else:
# 	print("меньше 0")

b = 'Г'

if b == 'А':
	c = "равно А"
elif b == 'Б':
	c = "равно Б"
elif b == 'В':
	c = "равно В"
else:
	c = "это я не знаю"

# print(c)


# *** условная задача "термостат"

# текущая температура
cur_temp = 11
# целевые значения температуры (установленная через ручку регулятора)
tar_temp_1 = 27
tar_temp_2 = 10
# дополнительное условие - "зависимость от присутствия людей"
z = False

# логика термостата
if z == True and cur_temp < tar_temp_1:
	print(f"Включен нагрев до {tar_temp_1}")
elif z == False and cur_temp < tar_temp_2:
	print(f"Включен нагрев до {tar_temp_2}")
else:
	print("Нагревание выключено")