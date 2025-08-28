# keywords => Mutable, Duplicate, Unordered, Heterogeneous

v = {}  # dictionary
a = {12, 13, 14, 15, 16, 12, 12}    # Set allows duplicate, but removes duplicate
print(a)
# a[0] = 100          # Set is unordered, no indexing

b = {1, True, "Rohan", 12.5, 5+6j, None}  # Heterogeneous
# Semi-heterogeneous, cannot store everything eg: list, tuple etc
print(b)

# Storing values in Python
a = 12
print(hash(a))     # hash function

b = "Rohan"
print(hash(b))

c = hash((1, 2, 3, 4, 5))
print(c)

# Hash value is different for same values
print(hash((1, 2, 3, 4, 5)))
print(hash((1, 2, 3, 4, 5)))

# Since sets are hashed, they are unordered
a = {12, 13, 14, 15, 16, 12, 12}
print(a)
# Lists and dictionaries are ordered thus not allowed in sets

# Set Basics
a = {1, 2, 3, 4, 5}

# Set Traversing
a = {1, 9, 2, 3, 4, 5}
for i in a:
    print(i)    # 1, 9, 2, 3, 4, 5 => 1, 2, 3, 4, 5, 9 (sets order numbers automatically)

# Set methods (add, remove, discard, pop, clear, union, intersection, difference, symmetric_difference)
s = {1, 2, 3, 4, 5}
s.remove(2)
print(s)

s.add(6)
print(s)

s.discard(7)
print(s)

s.pop()     # removes random element
print(s)    

s.clear()   # clear the set
print(s)

# Two set methods
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1.union(s2)       # s3 = s1 | s2
print(s3)

s1 = {1, 2, 3}
s2 = {2, 5, 6}
s3 = s1.intersection(s2)        # s3 = s1 & s2
print(s3)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}
s3 = s1.difference(s2)          # s3 = s1 - s2
print(s3)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1.symmetric_difference(s2)        # s3 = s1 ^ s2
print(s3)