# *** Основы объектно-ориентированного программрования (ООП) ***

# Объект обладает свойствами и методами (функции).
# Каждый объект должен принадлежать опредленному классу.
# Класс - это некий "чертеж" объектов.
# Объект определонного класса назвается экземпляром класса.

# Создание класса. Название класса принято писать с заглавной буквы.
class Cat:
    def __init__(self):
        # метод-конструктор

        # свойства (атрибуты, поля) - спец. переменная
        self.name = None

    def mur(self):
        # метод
        return f"Mur-mur! My name is {self.name}"

# Создание экземпляра (объекта) класса Cat
cat_1 = Cat()
cat_2 = Cat()

# Работа с свойствами (атрибутами)
# присвоение значения атрибуту
cat_1.name = "Barsik"
cat_2.name = "Murka"

# Чтение значения атрибута (свойства) name
# print(cat_1.name)
# print(cat_2.name)




# работа с методом

#вызов метода
# print(cat_1.mur())
# print(cat_2.mur())


# ***Наследование (принцип наследования)*** 

# создание родительского(предковый) класса
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

# Создание дочерних классов
class Insect(Animal):
    def __init__(self, num_legs):
        super().__init__(num_legs)
    
    def info(self):
        print(f"I am Insect. Legs: {self.num_legs}")

class Mammal(Animal):
    def __init__(self, num_legs):
        super().__init__(num_legs)
    
    def info(self):
        print(f"I am Mammal. Legs: {self.num_legs}")

# экземпляр класса Insect
bug = Insect(6)
bug.info()

# экземпляр класса Mammal
cat = Mammal(4)
cat.info()

class Human(Mammal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)
        self.name = name

    def hello(self):
        print(f"My name is {self.name}")

person_1 = Human(2, "John")

print(person_1.num_legs)
person_1.info()
person_1.hello()