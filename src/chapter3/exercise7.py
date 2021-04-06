#capture errors in case of wrong user input input
try:
    location = str(input('Enter Location: '))
    pay = float(input('Enter the pay: '))

#taking condition basing on user input for location and pay
    if location == 'kampala':
        if pay >= 10000000:
            print(location, "city")
            print('yes, Sure i will take the job.')
        else:
            print('No thanks, i can find something better!')
    elif location == 'mbarara':
        if pay >= 4000000:
            print(location, 'City')
            print('yes, Sure i will take the job')
        else:
            print("No thanks, can't work in Mbarara, i can find something better!")
    elif location == 'space':
        if pay >= 0:
            print(location, '!!')
            print('Without doubt, i will take the job in space')
        else:
            pass
    else:
        if pay >= 6000000:
            print(location, 'City')
            print('yes, Sure i will take the job at ', pay)
        else:
            print("Sorry, i can't take the job at ", pay)
except:
#return this message in case of any error
    print("Error!! something went wrong...")