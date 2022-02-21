i = 1
maximum = 1
secondmaximum = 1
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i > maximum: 
        secondmaximum = maximum
        maximum = i
        
else: 
    print("Maximum: " + "{}".format(maximum))
    print("Second Maximum: " + "{}".format(secondmaximum))