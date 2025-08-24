# keywords => Immutable, Duplicate, Ordered, Heterogeneous

a = (12, 13, 14, 15, 16, 12, 12)    # Tuple allows duplicate
print(a)
# a[0] = 100          # Tuple is immutable

b = (1, True, "Rohan", 12.5, 5+6j, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "a", 2: "b", 3: "c"}, print, None)  # Heterogeneous
print(b)

print(a[0])     # Indexing, Tuple is ordered
print(a[-1])

# Tuple Basics
a = (1, 2, 3, 4, 5)

#Indexing
print(a[0])
print(a[-1])

# Slicing
print(a[0:3])
print(a[2:5:1])  # start:stop:step

# Tuple Traversing
for i in range(len(a)):    # method using index
    print(a[i])

for i in a:    # method using direct value
    print(i)

'''
Tuples are immutable like strings, unlike lists.
Use Cases:
If you don't want to change the values of tuple, then use tuple.
'''

# Methods (Built-in functions)

t = (1, 2, 3, 4, 5)
print(t.count(5)) # count the number of 5 in the tuple
print(t.index(5)) # index of 5 in the tuple, first occurrence

# Tuple Unpacking
t = (1, 2, 3, 4, 5)
a, b, c, d, e = t
print(a, b, c, d, e)

a = (1)
print(type(a))  # Tuple with single element, becomes integer

a = (1,)
print(type(a))  # Tuple with single element, becomes tuple

# Swapping
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)