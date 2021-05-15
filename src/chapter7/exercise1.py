print('-------------------------------------------------------')
try:
    file1 = input('Enter file name: ')      # input file name to be worked on
    opfile = open(file1)    # opening the file

    for line in opfile:
        line = opfile.read()    # reading each line in the file
        line = line.upper()     # converting all the characters in the file to uppercase
    print(line)
except:
    print('File ', file1, 'does not exist')
