print("------------------------Eligibility to Vote-------------------------")
try:
    age = int(input('Enter your Age: '))
#conditioning for input of age
    if age >= 18:
        print('You can Vote!!')
    elif age > 0:
        print('Too young to Vote')
    elif age <= 0:
        print('You are a time traver')
    else:
        pass
except:
    print('INVALID INPUT, Enter your age')
