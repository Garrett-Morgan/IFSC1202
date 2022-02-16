i = 1
result = 1
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i > result: 
        result = i
else: 
    print("Maximum: " + "{}".format(result))