from os import path
print('-------------------------------------------------------')
check1 = 'na na boo boo'
file1 = input('Enter file name: ')  # input file name to be worked on.
file1 = file1.lower()   # Change to lowercase
if path.exists(file1):  # checking if the file entered exists in the current path
    file2 = open(file1)
    for line in file2:
        line = file2.readlines()
        line = len(line)    # counting the number of lines the file has
    print('There are', line, 'lines in the file')
elif file1 == check1:
    print("NA NA BOO BOO - You have been pranked! ")
else:
    print('File does not exist')
