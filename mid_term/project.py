# water utility billing software

def compute_gallons(a, b):  # Function for calculating the amount of water in gallons
    x = (b - a)
    if x < 0:
        x = (x + 999999999)     # when x value is a negative number, add it to last number 999999999
        x = (x + 1)/10  # then add 1 since meter has 9 digits which are 1 billion mathematically from 0 to 999999999
    else:
        pass
    return x


def final_display(a, b, c, d, f):   # Function for displaying customer detail
    print('--------------------------------------------------------------------------------')
    print('Customer Code: ', a)
    print('Customer Beginning Meter Reading: ', b)
    print('Customer Ending Meter Reading: ', c)
    print('Gallons of Water Consumed: ', d)
    print('Bill Amount: $', float(round(f, 2)))
    print('--------------------------------------------------------------------------------')


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

    while True:
        try:
            b_mtreading = int(input('Enter Beginning meter Reading: '))
            if b_mtreading >= 0 and b_mtreading <=999999999:
                break
            else:
                print('Meter reading exceeded range, try again!!')
        except ValueError:
            print('Input is invalid, try again!!')
    while True:
        try:
            e_mtreading = int(input('Enter ending meter Reading: '))
            if e_mtreading >= 0 and e_mtreading <= 999999999:
                break
            else:
                print('Meter number exceeded range, try again!!')
        except ValueError:
            print('Invalid input, try again')
    if customer_code in code1:
        if customer_code == code1[0]:   # check if the customer code 'r' for resident is there in the list
            if b_mtreading >= 0 and e_mtreading >= 0:
                gallons = compute_gallons(b_mtreading, e_mtreading)
                amount = 5 + (gallons*0.0005)
                final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
            else:
                print('Meter reading not a positive number, try again!!')
        if customer_code == code1[1]:   # check if the customer code 'c' for commercial is there in the list
            if b_mtreading >= 0 and e_mtreading >= 0:
                gallons = compute_gallons(b_mtreading, e_mtreading)
                if gallons <= 4000000:
                    amount = 1000
                    final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
                elif gallons > 4000000:
                    amount = 1000 + ((gallons-4000000)*0.00025)
                    final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
            else:
                print('Meter reading not a positive number, try again!!')
        if customer_code == code1[2]:   # checking if the customer code 'i' for industrial is in the list
            if b_mtreading >= 0 and e_mtreading >= 0:
                gallons = compute_gallons(b_mtreading, e_mtreading)
                if gallons <= 4000000:
                    amount = 1000
                    final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
                elif gallons > 4000000 and gallons <= 10000000:
                    amount = 2000
                    final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
                elif gallons > 10000000:
                    amount = 2000 + ((gallons-10000000)*0.00025)
                    final_display(customer_code, b_mtreading, e_mtreading, gallons, amount)
            else:
                print('Meter reading not a positive number, try again!!')
print('------------------------------------------------------------------------------')
print('Bye... \n******(C) Group 6*****')
