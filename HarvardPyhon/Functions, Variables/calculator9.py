# Demonstrates rounding after the decimal point

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)
#round 3.5 ---> 4
print(z)
