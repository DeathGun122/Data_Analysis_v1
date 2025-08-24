# keywords => Mutable, Duplicate, Unordered, Heterogeneous

v = {}  # dictionary
a = {12, 13, 14, 15, 16, 12, 12}    # Set allows duplicate, but removes duplicate
print(a)
# a[0] = 100          # Set is unordered, no indexing

b = {1, True, "Rohan", 12.5, 5+6j, None}  # Heterogeneous
# Semi-heterogeneous, cannot store everything eg: list, tuple etc
print(b)

