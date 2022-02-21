i = 1
result = 1
count = 0
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i > result: 
        result = i
    if i == result:
        count = count + 1
else: 
    print("Maximum: " + "{}".format(result))
    print("Number of Occurences: " + "{}".format(count))