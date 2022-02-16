i = 1
result = 0
sum = 0
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i > result: 
        result = i
        sum = sum + 1
else: 
    print("Maximum: " + "{}".format(result))
    print("Index of Maximum is: " + "{}".format(sum))