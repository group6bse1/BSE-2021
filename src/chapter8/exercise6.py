num_list = []
while True:
    num1 = input('Enter a number: ')
    if str(num1).lower() == 'done':
        break
    elif float(num1) <= 0 or float(num1) >= 0:
        num_list.append(float(num1))
print('Maximum: ', max(num_list))
print('Minimum: ', min(num_list))
