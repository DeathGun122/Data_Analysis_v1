# Hiding internal details and showing what is needed

class Factory:
    _a = "Pune"     # Protected (naming convention for developers)
    __b = "Private"     # Private 
    def show(self):
        print("Hello from Pune Factory")

obj = Factory()

print(obj._a)

# Access Modifier - Public, Private, Protected

# Public 
class Bhopal(Factory):
    def show2(self):
        print(super()._a)

obj = Bhopal()
obj.show2()
