# Objects => Data + Methods
# Data => Attributes
# Methods => Functions

class Factory:
    a = 123
    def hello(self):
        print("Hello World")
    
    print("Hello World")

obj = Factory()         # Object (Instance of a class)
obj2 = Factory()        # Object 2nd


obj.hello()
print(obj.a)

