def gallons(a, b):   # Computing gallons used by customer.
    # a is the initial meter reading
    # b is the final meter reading 
    c = (b-a)
    if c < 0:
        c = (c + 1000000000)/10     # add 1 billion to 'c' since from 0 to 999999999 is 1 billion times on the meter
    else:
        pass
    return c


def bill(g, f, l, a, p):    # Final display
    print('------------------------------------------------------------')
    print("Customer's code: ", g)
    print("Beginning meter reading: ", f)
    print("Ending meter reading: ", l)
    print("Gallons of water used by customer: ", a)
    print("Amount billed to customer: $", float(round(p, 2)))


print("--------------------WATER BILLING SOFTWARE-----------------------")
codes1 = ['r', 'c', 'i']
while True:
    code = str(input("Please enter customer's code: "))   # Customer's code e.g c,r,i
    code = code.lower()   # accepting any letter case and converting it to standard lower case
    if code not in codes1:
        break
    else:
        pass
    initial = int(input("Please enter beginning meter reading: "))
    final = int(input("Please enter ending meter reading: "))

    if code == codes1[0]:   # computing residential bill
        if initial >= 0 and final >= 0:
            Gallons = gallons(initial, final)
            Bill = 5.00 + (Gallons*0.0005)
            bill(code, initial, final, Gallons, Bill)
    elif code == codes1[1]:     # computing commercial bill
         if initial >= 0 and final >= 0:
            Gallons = gallons(initial, final)
            if Gallons <= 4000000:
                Bill = 1000
                bill(code, initial, final, Gallons, Bill)
            elif Gallons > 4000000:
                Bill = (1000 + (0.00025*(Gallons-4000000)))
                bill(code, initial, final, Gallons, Bill)
    elif code == codes1[2]:     # computing industrial bill
        if initial >= 0 and final >= 0:
            Gallons = gallons(initial, final)
            if Gallons <= 4000000:
                Bill = 1000
                bill(code, initial, final, Gallons, Bill)
            elif Gallons > 4000000 and Gallons <= 10000000:
                Bill = 2000
                bill(code, initial, final, Gallons, Bill)
            elif Gallons > 10000000:
                Bill = (2000 + (Gallons-10000000)*0.00025)
                bill(code, initial, final, Gallons, Bill)
    else:
        pass
print('------------------------------------------------------------')
print("Thank you....")
print('   (c) Group 6    ')