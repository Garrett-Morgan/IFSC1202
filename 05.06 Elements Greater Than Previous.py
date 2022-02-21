i = 1
sum = 0
counter = 0
while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    if sum < i and sum != 0:
        counter = counter + 1
    sum = i
else: print("Number of Values Greater than the Previous: " + "{}".format(counter))