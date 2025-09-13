class Animal:
    name = 'lion'         # class attribute
    age = 10        

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def show(self):         # instance method
        print(self.name)
        print(self.age)

# class method (used my decorator @classmethod)
    @classmethod
    def info(cls):
        print(cls.name)
        print(cls.age)

    # self targets the current object, cls targets the class

# static method (used my decorator @staticmethod)
    @staticmethod            # static method (accesses no class or objects)
    def hello():
        print("Hello World")

