print("------------------------Eligibility to Vote-------------------------")
try:
    age = int(input('Enter your Age: '))
#conditioning for input of age to tell if someone of a certain age can vote
    if age >= 18:
        print('You can Vote!!')
    elif age > 0:
        print('Too young to Vote')
    elif age <= 0:
        print('You are a time traver')
    else:
        pass
except:
#return this message in case of any errors that will occur during execution
    print('INVALID INPUT, Enter your age')
