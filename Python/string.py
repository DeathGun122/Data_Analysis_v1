# String take a lot of memory
# string is immutable
# string is a sequence

a = 'A'
print(ord(a))   # Unicode
print(chr(65))  # ASCII to character

# Indexing
b = 'Rohan'
print(b[0])   # Positive indexing
print(b[-1])  # Negative indexing

# Slicing (start:stop:step)
print(b[0:3])
print(b[2:])
# stop index is exclusive
print(b[:3])
# Everything is optional
print(b[::])

# Reserving
print(b[::-1])