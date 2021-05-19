#   open, read and change each line of the file into a list
print('*************program Initiating*************************')

f_name = input('Enter file name: ')
op_file = open(f_name)

for line in op_file:
    op_file.readlines(4)
    x_file = line.split()
    x_file.sort()
    print(x_file)
print('---------------------------------------------------------')
