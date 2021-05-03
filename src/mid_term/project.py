# water utility billing software

print('                         Water Billing System                         ')
print('------------------------------------------------------------------------------------')
code1 = ['r', 'c', 'i']

while True:
    customer_code = input('Enter Customer Code: ')
    customer_code = customer_code.lower()  # changing any possible customer codes in uppercase to lowercase
    if customer_code not in code1:
        break
    else:
        pass
    try:
        b_mtreading = int(input('Enter Beginning meter Reading: '))
        e_mtreading = int(input('Enter ending meter Reading: '))
    except:
        print('Invalid meter reading!!')
        continue
    break
print('------------------------------------------------------------------------------')
print('Bye...')
