#handling any errors that might occur during execution if user input is wrong
try:
    # accepting Hours from user which is an integer
    hours = float(input('Please enter hours: '))

    # accepting rate per hour from the user which is float value-
    rate = float(input('please enter rate :'))

    if hours > 40:
    #calculating the gross pay if hours worked are more than 40
        pay = hours * (1.5 * rate)
    else:
    #calculating the gross pay if hours are less than 40
        pay = hours * rate

    #printing the gross pay after the above computation
    print('Gross pay: ', pay)
#below is my capture of any errors that  will occur during execution or wrong user input
except:
    print('INVALID INPUT, Enter a numerical value!!')