print('---------------------MAXIMUM AND MINIMUM VALUE---------------------')
nam_list = []
count = 0
total = 0
#use of the while loop for value being input is true
while True:
    nam = input('Enter a number: ')
    if str(nam) == 'done' or str(nam) == 'DONE':
        break
    try:
        count = count + 1
        total = total + int(nam)
        nam_list += [int(nam)]  #creating a list of all numbers being input
    except:
        print("invalid input")

max1 = max(nam_list)    #getting the maximum value from the list
min1 = min(nam_list)    #getting the minimum value from the list

print('------------------------------------------------------------------')
print('Total: ', total)
print('Count: ', count)
print('List of Numbers is: ', nam_list)
print('Maximum number is: ', max1)
print('Minimum number is: ', min1)