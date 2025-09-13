# constructor => a special method that is called when an object is created
# self => keyword that refers to the current object, targets the location of the object

# Inputs in classes and methods (parameters are not predefined)

class Factory:
    def __init__(self, material, zips, pockets):   # constructor (dunder method) / initialization function
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(self.material)
        print(self.zips)
        print(self.pockets)

reebok = Factory("Leather", 10, 5)               # Object
campus = Factory("Resins", 5, 2)               # Object

reebok.show()
campus.show()

