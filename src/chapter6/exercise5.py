str1 = 'X-DSPAM-Confidence: 0.8475 '
str2 = str1.find(' ')   # obtaining the position of the first space in string
print('Sting is: ', str1)
print('Length: ', len(str1))
x = str2 + 1    # position of space plus is equal to the position of the first digit of 0.8475
y = str1[x:len(str1)]   # extracting the number 0.8475
y = float(y)    # converting the string to float
print('Number is: ', y)
