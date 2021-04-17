#function for computing investment value

def investment(c, r, t, n):
    p = c*(1+(r/n))**(t*n)
    return p

c = int(input('Enter initial amount of investment: '))
r = float(input('Yearly rate on interest: '))
t = int(input('Number of years till maturity: '))
n = int(input('Number of times interest is compounded per year: '))
invest = investment(c, r, t, n) #calling the function investment
print('Your Final Investment is: ', round(invest, 2))