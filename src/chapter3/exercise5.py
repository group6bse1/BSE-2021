print('----------------------Wedding Costs computation-------------------')
#capture any error messages for wrong input
try:
    n_people = int(input('Enter number of people: '))
#conditioning for input from the user
    if n_people <= 50:
        print('Price for Wedding catering is $4,000')
    elif n_people <= 100:
        print('Price for Wedding catering is $10,000')
    elif n_people <= 200:
        print('Price for Wedding catering is $15,000')
    elif n_people > 200:
        print('Price for Wedding catering is $20,000')
    else:
        pass
except:
#return for any error messages
    print('INVALID INPUT, Please Enter the number of people')