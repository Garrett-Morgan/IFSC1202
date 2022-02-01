x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if(x < y):
    if (x < z): print("{}".format(x))    
if(y < x):
    if (y < z): print("{}".format(y))
if(z < x):
    if (z < y): print("{}".format(z))
