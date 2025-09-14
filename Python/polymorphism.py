def show():
    print("Hello")

def show():
    print("Hello World")

show()

# Method Overwriting
class Animal:
    def show(self):
        print("Hello World")

class Human(Animal):
    def show(self):
        print("Hello from Human")

obj = Human()
obj.show()

# Method Overloading does not exist in python

# Duck Typing: If it walks and quacks like a duck, it might be a duck.

class Factory:
    def display(self):
        print("Hello form Factory")

class Mall:
    def display(self):
        print("Hello form Mall")

obj = Factory()
obj2 = Mall()

obj.display()
obj2.display()