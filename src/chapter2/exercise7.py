#input amount to be changed from user
amount = float(input("Enter amount for change: "))
#for notes available for amount to change with $100 the highest
x = amount//100
print(x, " one hundreds")

amount = amount-(x*100)
x = amount//50
print(x, "Fifties")

amount = amount-(x*50)
x = amount//20
print(x, "twenties")

amount = amount-(x*20)
x = amount//10
print(x, "tens")

amount = amount-(x*10)
x = amount//5
print(x, "fives")

amount = amount-(x*5)
x = amount//1
print(x, "ones")
#for coins available as the smallest denomination for the given amount to change
amount = amount-(x*1)
x = amount//0.25
print(x, "quarters")

 amount = amount-(x*0.25)
x = amount//0.1
print(x, "dimes")

amount = amount-(x*0.1)
x = amount//0.05
print(x, "nickels")

amount = amount-(x*0.05)
x = amount//0.01
print(x, "pennies")


