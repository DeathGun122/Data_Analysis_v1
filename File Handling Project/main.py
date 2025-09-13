from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    # recursive glob function
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i+1}: {items}')

def createFile():
    try:
        print('Existing Files and Folders:')
        readFileAndFolder()

        name = input("Enter the name of the file: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Write data in the file: ")
                fs.write(data)

            print(f"File created successfully")
        else:
            print("File already exists.")

    except Exception as err:
        print(f'Error {err} occured.')

def readFile():
    try:
        print('Existing Files and Folders:')
        readFileAndFolder()

        name = input("Which file do you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            
            print(f"File read successfully")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f'Error {err} occured.')

def updateFile():
    try:
        print('Existing Files and Folders:')
        readFileAndFolder()

        name = input("Which file do you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print('Press 1 for changing the file name.')
            print('Press 2 for overwriting the data of your file.')
            print('Press 3 for appending some content to your file.')

            res = int(input("Enter your choice: "))

            if res == 1:
                name2 = input("Enter the new name of the file: ")
                p2 = Path(name2)
                p.rename(p2)
                print(f"File name changed successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Write data in the file to be overwritten: ")
                    fs.write(data)

                print(f"File updated successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Write data in the file to be appended: ")
                    fs.write('\n' + data)

                print(f"File updated successfully")

            else:
                print("Invalid choice.")      

    except Exception as err:
        print(f'Error {err} occured.')

def deleteFile():
    try:
        print('Existing Files and Folders:')
        readFileAndFolder()

        name = input("Which file do you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"File deleted successfully")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f'Error {err} occured.')

print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating a file.")
print("Press 4 for deleting a file.")

check = int(input("Enter your choice: "))

if check == 1:
    createFile()

elif check == 2:
    readFile()

elif check == 3:
    updateFile()

elif check == 4:
    deleteFile()

else:
    print("Invalid choice.")