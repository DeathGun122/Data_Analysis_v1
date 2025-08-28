# File => Any data stored in a file is called a file with extension

# CRUD operations => File handling
# 1. Create
# 2. Read
# 3. Update
# 4. Delete

# open
# p = open(r'Python\hello.txt')
# print(p.read())

# creating a file
r = open(r'Python\superman.txt','w')
r.write("Hello World")
r.close()

# append
r = open(r'Python\superman.txt','a')
r.write("\nHello World")
r.close()

# x => create file if not exists
r = open(r'Python\superman.txt','x')
r.write("\nHello World")
r.close()