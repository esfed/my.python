# *** Функции ***

# Функции - это некая "фабрика", которая на вход получает (не всегда) данные 
# и на выходе возвращает (не всегда) другие (переработанные) данные.

# 1 вариант. Функция, которая не принимает ничего и ничего не возвращает

# опредение (создание) функции с именем "func_1"
def func_1():
	name = "John"
	print(name)

# вызов функции с именем "func_1"
# func_1()

# отправление объекта функции с именем "func_1"
# print(func_1)


# 2 вариант. Функция, принимающая данные, но не возвращающая данные

# Если функция должна принимать на вход данные,
# то при определении функции нужно определить аргументы
def func_2(arg_1, arg_2):
	result = arg_1 + arg_2
	print(result)

# вызов функции с передачей параметров (значений) (позиционная передача параметров)
# func_2(100, 20)

# Определение функции с аргументами, два из которых имеют значения по умолчанию
def func_3(c, a=10, b=20):
	res = a + b + c
	print(res)

# позиционная передача параметров 
# (второй параметр замещает значение по умолчанию у второго аргумента)
# func_3(100, 200)

# именованная передача параметров
# func_3(10, b=100)


# Аргумент, для множественных позиционных параметров
def func_4(*args):
	print(args)
	print(args[0])
	print(args[1])
	print(args[-1])
	res = 0
	for val in args:
		res += val
	print(res)

# func_4(100, 20, 3, 1000, 777)

# Аргумент, для множественных именованных параметров
def func_5(**kwargs):
	print(kwargs)

# func_5(x=10, y=5, hello=777)


# 3 вариант. Функция, возвращающая значение
def func_6(name, age):
	s = f"Имя: {name}, Возраст: {age}"
	return s

# print(func_6("Peter", 25))


# *** безымянные функции (лямда-выражение, лямда-функции) ***

# Создание лямбда-выражение
# особенности:
#  - всегда имеет аргумент (-ы) (вход)
#  - всегда возвращает результат (выход)
my_lambda = lambda x, y: x ** y

# print(my_lambda(10, 3))


# лямбда-выражение внутри генератора списка
my_list = [(lambda arg: arg + 5)(item) for item in range(10)]

# print(my_list)

# лямбда-выражение внутри списка
lambda_list = [lambda a, d: a + b, lambda a, b: a - b, lambda a, b: a * b]

# print(lambda_list[2](10, 5))

# *** Декараторы ***

# это функции, декорирующие другие функции,
# т.е. добавляющие дополнительную функциональность

# определение декоратора
# def my_decorator(func_obj):
# 	# определение функции-обертки
# 	def wrapper():
# 		# вызов целевой функции (декорируемой)
# 		func_obg()
# 		# возврат объекта функции-обертки
# 	return wrapper

# целевая (декориремая) функция
# def  target_funk()
#	print ("Helll")


# *** Пример. Калькулятор ***

# Определение функции нашего калькулятора
def calculate(a, b, cmd):
	if cmd  == '+':
		result = a + b
	elif cmd == '-':
		result = a - b
	elif cmd == '*':
		result = a * b
	elif cmd == '/':
		result = a / b
	else: 
		result = f"Что это {cmd}?"
	return result

print("Hello! I am your Calculator :)")

while True:
	num_1 = int(input("Enter 1 number: "))
	num_2 = int(input("Enter 2 number: "))
	cmd = input("Enter the operation name: ")

	if cmd == "stop":
		print("Buy buy!")
		break
	else:
		res = calculate(num_1, num_2, cmd)
		print(f"Result = {res}")





