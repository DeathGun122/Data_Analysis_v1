# Inheritance => a special method that allows one class to inherit the properties and methods of another class

class Factory:                          # Parent class/superclass
    a = "from class Factory"
    def hello(self):
        print("Hello from class Factory")

class new_Factory(Factory):             # Child class/subclass
    pass

obj = new_Factory()
obj.hello()
print(obj.a)

# Constructor in inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print('Animal name is', self.name, '.')

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)          # call parent constructor
        self.age = age

    def show(self):                     # override parent method
        print('Age is', self.age, '.')

obj = Human('Rohan', 19)
obj.show()

# Single level inheritance => only one level of inheritance
# Multilevel inheritance => multiple levels of inheritance

# Multiple inheritance

class Animal:
    def __init__(self, name):
        pass

class Human:
    def __init__(self, name, age):
        pass

    name3 = "R2D2"

class Robots(Human, Animal):
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

obj = Robots(Human, Animal)
print(obj.name1)
print(obj.name2)
print(obj.name3)

# Multi level inheritance (grandparent class -> parent class -> child class)

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class Fact_Bhopal(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class Fact_Pune(Fact_Bhopal):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = Fact_Pune("steel", 4, "blue", 2)
print(obj.material)
print(obj.zips)
print(obj.color)
print(obj.pockets)

