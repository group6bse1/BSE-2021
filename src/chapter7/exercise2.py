count = 0
total = 0
print('-------------------------------------------------------')
try:
    file1 = input('Enter file name: ')  # input file name to be worked on
    op_file = open(file1)  # opening the file
    for line in op_file:
        line = op_file.readline()  # reading each line in the file
        if line.startswith('X-DSPAM-Confidence:'):
            x = line.find(' ')  # start point for extracting the numbers
            y = float(line[x:27])   # extracting the numbers while converting to float
            count = count + 1       # counting the number of lines with the extracted content
            total = total + y       # getting the total of all the extracted float numbers
    print('count is: ', count)
    print('total is: ', total)
    Average = total/count
    print('Average spam Confidence: ', Average)
except:
    print('File', file1, 'does not exist')
