import sys
#vending machine algorithm
def centds(a):
    #function for breaking the price into dollars and cents
    x = float(a)//1
    y = (float(a)%1)*100
    print('Amount due is: ', int(x),'dollars and ',int(y) ,'cents')

nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

print('                  Welcome to vending machine change maker                 ')
print('--------------------------------------------------------------------------')
print('****Stock contains****')
#content of stock present
print(nickels, 'Nickels')
print(dimes, 'Dimes')
print(quarters, 'Quarters')
print(ones, 'Ones')
print(fives, 'Fives')

#Area for checking validity of price input
#Request for purchase price from the user.

while True:
        price1 = input('Enter purchase price or "q" to quit: ')
        try:
            if price1 == 'q' or price1 == 'Q':
                sys.exit()
            elif round(float(price1) % 0.05, 2) != 0.05:
                if round(float(price1) % 0.05, 2) < 0:
                    continue
                print('Illegal Input, Enter price which a multiple of 5 Cents and is a non-negative!!')
            break
        except:
            print('Invalid input, try again!!')

#Section for deposits made.

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
#verifing if input is correct
while True:
    deposit = input('Indicate your deposit: ')
    if str(deposit) in menu_list:
        break
    else:
        print('illegal entry, try again!!')
q = quarters
d = dimes
n = nickels
o = ones
f = fives
c = 'c'

if deposit == 'q':
    deposit = q
elif deposit == 'd':
    deposit =d
elif deposit == 'n':
    deposit = n
elif deposit == 'o':
    deposit = o
elif deposit == 'f':
    deposit = f
#elif deposit == 'c':
#    deposit = c

while True:
    if deposit == float(price1):
        print('The is same as:', deposit)
    elif deposit == menu_list[5]:
        print('coucil')
        #call the change dispenser function: to be continued
    elif deposit > float(price1):
        print("Deposit is greater", deposit)
        #call the change dispenser function: to be continued
    elif deposit < float(price1):
        print('deposit is lesser', deposit)
        #call change dispenser function: to be continued

        #call change dispenser function: to be continued
    break

print('Program to be continues....')
