x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if(x == y):
    if(y != z): print("3")
if(x == z):
    if(x != y): print("2")
if(y == z):
    if(x != y): print("1")

