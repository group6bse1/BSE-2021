print('*************program Initiating*************************')
count = 0
f_name = input('Enter file name: ')
op_file = open(f_name)

for line in op_file:
    op_file.readline()
    if line.startswith('From '):
        x_file = line.split()
    count = count + 1
    print(x_file[1])
print('There were', count, 'lines that start with "From" word')
print('---------------------------------------------------------')
