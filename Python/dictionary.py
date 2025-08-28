# dictionary => Hash Map in other languages
# keys => Unique, Immutable, Insertion Order
# values => Mutable, Heterogeneous

d = {}
print(type(d))

d = {1: "Hello", 2: "World", 3: "Python"}
print(d)
print(d[1])
print(d[2])
print(d[3])

# mutable (value can be changed but keys cannot be changed)
d[1] = "Rohan"
print(d)
d = {1: "Hello", 2: "World", 3: "Python"}
print(d)
d[4] = "Rohan"
print(d)

# key values are index of list
d = {1: "Hello", 2: "World", 3: "Python"}
print(d.keys())
print(d.values())
print(d.items())

# CRUD => Create, Read, Update, Delete
d = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

d.update({60: 600, 70: 700})        # Insert/Update
print(d)
d[80] = 800                         # Insert/Update 2nd way
print(d)                    

del d[30]                           # Delete
print(d)

d.clear()                           # Clear
print(d)

# Dictionary Traversing
d = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}
for i in d:
    print(i, d[i])                  # i = key, d[i] = value

for i in d.values():
    print(i)

for i in d.keys():                  # i = key (Default)
    print(i)

# Deep copy & Shallow copy
a = [1, 2, 3, 4, 5]
b = a                               # Deep copy (any copy will be available in both)

b[0] = 100
print(a)
print(b)

a = [1, 2, 3, 4, 5]
b = a.copy()                        # Shallow copy
b[0] = 100
print(a)
print(b)

# dictionary methods
d = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

# copy
d1 = d.copy()
print(d1)

# get
print(d.get(10))                    # returns 100
print(d.get(60))                    # returns None (KeyError)

# pop
print(d.pop(10))                    # returns 100
print(d)

# popitem
print(d.popitem())                  # returns (50, 500)
print(d)

# update
d1 = {60: 600, 70: 700}
d.update(d1)
print(d)

# clear
d.clear()
print(d)

# items
d = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}
print(d.items())

# keys
print(d.keys())

# Question 1
d1 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}
d2 = {60: 600, 70: 700}

for i in d2:
    d1[i] = d2[i]

print(d1)

# Question 2
d1 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}
sum = 0
for i in d1.values():
    sum += i
print(sum)

# Question 3
a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7,7 ,8,8,8,8,9,9,9]
d= {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# Question 4
d1 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600, 70: 700}
d2 = {50: 500 ,60: 600, 70: 700}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)