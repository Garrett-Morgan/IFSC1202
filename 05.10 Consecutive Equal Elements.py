i = 1
result = 1
count = 0
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if i == result:
        count = count + 1
        commonnumber = i 
    result = i
else: 
    print("Maximum: " + "{}".format(commonnumber))
    print("Number of Occurences: " + "{}".format(count))