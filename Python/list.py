# keywords => Mutable, Duplicate, Ordered, Heterogeneous

a = [12, 13, 14, 15, 16, 12, 12]    # List allows duplicate
print(a)
a[0] = 100          # List is mutable
print(a)

b = [1, True, "Rohan", 12.5, 5+6j, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "a", 2: "b", 3: "c"}, print, None]  # Heterogeneous
print(b)

print(a[0])     # Indexing, List is ordered
print(a[-1])

# List Basics
a = [1, 2, 3, 4, 5]

#Indexing
print(a[0])
print(a[-1])

# Slicing
print(a[0:3])
print(a[2:5:1])  # start:stop:step

# List Traversing
for i in range(len(a)):    # method using index
    print(a[i])

for i in a:    # method using direct value
    print(i)


'''
Note:
Functions => It is a block of code which is written to perform a specific task and can be called multiple times
Methods => It is a block of code which is written to perform a specific task and can be called only once. 
           It is a function inside a class. e.g. list.sort, list.reverse, list.append
'''

# print(dir(list)) 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

l = [1, 2, 3, 4, 5]
l.append(6) # add 6 at the end
print(l)

l.insert(2, 100) # insert 100 at index 2
print(l)

l.reverse() # reverse the list
print(l)

l.sort() # sort the list
print(l)

l.remove(100) # remove 100 from the list, first occurance
print(l)

l.pop() # remove the last element from the list, by default it removes the last element
print(l)

var = l.pop(2) # remove the element at index 2
print(l)
print(var)

l.clear() # clear the list
print(l)

l = [1, 2, 3, 4, 5]
l2 = l.copy() # copy the list
print(l2)

l = [1, 2, 3, 4, 5]
l2 = l.count(5) # count the number of 5 in the list
print(l2)

l = [1, 2, 3, 4, 5]
l2 = l.index(5) # index of 5 in the list
print(l2)

l = [1, 2, 3, 4, 5]
l2 = l.copy() # copy the list
print(l2)

# Question 1
l = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print("Positive numbers:")
for i in l:
    if i < 0:
        print(i)

print("Negative numbers:")
for i in l:
    if i > 0:
        print(i)

# Question 2
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum = 0
for i in l:
    sum += i
print(f'Mean of all numbers: {sum/len(l)}')

# Question 3
l = [12, 36, 14, 19, 10, 99, 56]
max = l[0]
index = 0
for i in range(1, len(l)):
    if l[i] > max:
        max = l[i]
        index = i
print(f'Maximum number: {max} at index: {index}')

# Question 4
l = [12, 36, 14, 19, 10, 99, 56]
max = l[0]
max2 = l[0]
for i in range(1, len(l)):
    if l[i] > max:
        max2 = max
        max = l[i]
    elif l[i] > max2:
        max2 = l[i]
print(f'Second largest number: {max2}')

# Question 5
l = [1, 2, 3, 6, 5]
count = 0
for i in range(1, len(l)):
    if(l[i] < l[i-1]):
        count += 1

if count == 0:
    print('Array is sorted')
else:
    print('Array is not sorted')