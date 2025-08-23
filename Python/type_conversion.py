# str()
a = 10
print(type(a))
b = str(a)
print(type(b))

# int()
a = "10"
print(type(a))
b = int(a)
print(type(b))

# float()
a = "10.5"
print(type(a))
b = float(a)
print(type(b))

# complex()
a = "10+5j"
print(type(a))
b = complex(a)
print(type(b))

# bool()
a = "True"
print(type(a))
b = bool(a)
print(type(b))
print(b)

num = 12
print(type(num))

num = bool(num)
print(type(num))
print(num)

# Falsy values : False, None, 0, 0.0, 0j, "", (), [], {} results in False
num1 = 0
print(type(num1))

num1 = bool(num1)
print(type(num1))
print(num1)

# Implicit type conversion
a = 10
b = 20.5
c = a + b
print(type(c))
print(c)

a = 12/3
print(type(a))
print(a)

# Explicit type conversion
a = 10
b = str(a)
print(type(b))
print(b)