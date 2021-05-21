from os import path
in_file = input('Enter a file name: ')  # file to copy data data too
if path.exists(in_file):    # Check if file does exist in the active directory
    in_file1 = open(in_file, "w")
    for line in in_file:
        del line            # delete all the data in the file
else:
    in_file1 = open(in_file, "w")
year = str(input("Enter year: "))   # year to be searched in the file by full year, or prefix
in_file2 = open('measles.txt')      # opening file to copy from data
in_file2.readline()
if year.lower() == 'all':
    for line in in_file2:
        in_file1.write(line)
elif year:
    for line in in_file2:
        if year in line[85:]:
            in_file1.write(line)    # copying the needed data from measles file to new file input

in_file1.close()
in_file2.close()
