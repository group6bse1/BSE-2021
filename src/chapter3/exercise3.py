try:
    # request score from user between 0.0 and 1.0
    score = float(input('Enter the score: '))

    #setting conditions for score in the range of 0.0 to 1.0
    if 0.0 <= score <= 1.0:
        if score < 0.6:
            print('Your score is "F"')
        elif score >= 0.6:
            print('Your score is "D"')
        elif score >= 0.7:
            print('Your score is "C"')
        elif score >= 0.8:
            print('Your score is "B"')
        elif score >= 0.9:
            print('Your score is "A"')
        else:
            pass
    else:
        print('Error, you have exceeded the score range')
        print('input score between 0.0 and 1.0')

#capting any errors that may arise due to wrong user input
except:
    print('Error, no such score')
    print('INVALID INPUT, enter a score between 0.0 and 1.0')