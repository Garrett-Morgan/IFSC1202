i = 1
sum = 0
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i != 0:
        even = i % 2
        if even == 0: 
            sum = sum + 1
else: 
    print("Number of Even Values: " + "{}".format(sum))