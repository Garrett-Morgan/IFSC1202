x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if( x < y ):
    if(x < z):
        if( y < z ): print("{}".format(x) + " " + "{}".format(y) + " " + "{}".format(z))
        if( z < y ): print("{}".format(x) + " " + "{}".format(z) + " " + "{}".format(y))
if( y < x ):
    if(y < z):
        if( x < z ): print("{}".format(y) + " " + "{}".format(x) + " " + "{}".format(z))
        if( z < x ): print("{}".format(y) + " " + "{}".format(z) + " " + "{}".format(x))
if( z < x ):
    if(z < y):
        if( x < y ): print("{}".format(z) + " " + "{}".format(x) + " " + "{}".format(y))
        if( y < x ): print("{}".format(z) + " " + "{}".format(y) + " " + "{}".format(x))
