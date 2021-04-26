import sys
# vending machine algorithm
def centds(a):
    # function for breaking the price into dollars and cents
    x = float(a)//1
    y = (float(a) % 1)*100
    print('Amount due is: ', int(x),'dollars and ',int(y) ,'cents')

def coins(a):
    # function for allocation of coin/bills to be entered by user
    if a == 'q' or a == 'Q':
        x = 0.25
    elif a == 'd' or a == 'D':
        x = 0.1
    elif a == 'n' or a == 'N':
        x = 0.05
    elif a == 'o' or a == 'O':
        x = 1
    elif a == 'f' or a == 'F':
        x = 5
    else:
        pass
    return x

nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
total = 0
print('                  Welcome to vending machine change maker                 ')
print('--------------------------------------------------------------------------')
print('****Stock contains****')
# content of stock present
print(nickels, 'Nickels')
print(dimes, 'Dimes')
print(quarters, 'Quarters')
print(ones, 'Ones')
print(fives, 'Fives')

# Area for checking validity of price input
# Request for purchase price from the user.

while True:
        price1 = input('Enter purchase price or "q" to quit: ')

        if str(price1) == 'q' or str(price1) == 'Q':
                sys.exit()
        try:
            if round(float(price1) % 0.05, 2) == 0.05:
                if round(float(price1) % 0.05, 2) > 0:
                    break
            print('Illegal Input, Enter price which a multiple of 5 Cents and is a non-negative!!')
            continue
        except:
            print('Invalid input, try again!!')

# Section for deposits made.

print('----------------------------------------------------------------------')
print('Menu of deposits:')
print("'q' - deposit a quarter")
print("'d' - deposit a dime")
print("'n' - deposit a nickel")
print("'o' - deposit one dollar")
print("'f' - deposit five dollars")
print("'c' - cancel deposit")

centds(price1)

menu_list = ['q','d','n','o','f','c']
# verifying if input is correct
while True:
    deposit = input('Indicate your deposit: ')
    if deposit in menu_list:
        if deposit == menu_list[5]:
            total = (total + coins(deposit))//0.25
            print(total, 'Quarter')
        if coins(deposit) < float(price1):
            total = total + coins(deposit)
            if total > float(price1):
                total = total - float(price1)
                print(int(total//0.25), 'Quarters')
            elif total == float(price1):
                print('No change')
            continue
        if coins(deposit) > float(price1):
            total = total + coins(deposit)
            total = total - float(price1)
            print(': ', int(total//0.25), ' : Quarters')
        if coins(deposit) == float(price1):
            total = total + coins(deposit)
            print('No change')

        break
    else:
        print('illegal entry, try again!!')


