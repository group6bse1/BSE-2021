#Getting input from user for c,r,t,n for computing p
c = float(input("Enter the initial amount of Investment: "))
r = float(input("Enter the rate of interest in %: "))
t = float(input("Enter the period of investment in years: "))
n = float(input("Enter number of times compounded: "))

#formula for computing the final value of investment which is p
p = c*(1+r/n)**(t*n)

#printing the final value
print("Final value of investment is: ", round(p, 2))
