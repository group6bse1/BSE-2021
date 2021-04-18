#creating a function to compute pay
def compute_pay(a,b):
#'a' is the hours worked and 'b' is the rate of pay
#assuming the standard time for working in a day is 8 hours but then an employee works past that time, then we multipy rate by 1.5
    if a <= 8:
        compt = a * b
    elif a > 8:
        compt = a * (b * 1.5)
    else:
        print('No time worked!!')

    return compt
try:
    hours=float(input('Please enter hours: '))
    rate=float(input('Please enter rate:'))
except:
    print('Invalid input, Please input numerical values.')
try:
    x=compute_pay(hours, rate)
except:
    print('Improper usage of function ')
print('The pay is : ', x)


