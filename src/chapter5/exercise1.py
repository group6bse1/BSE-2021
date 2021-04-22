print('---------------------TOTAL, COUNT AND AVERAGE---------------------')
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
    except:
        print("invalid input")

#calculation of average
average = total/count
print('------------------------------------------------------------------')
print('Total: ', total)
print('Count: ', count)
print('Average: ', average)



