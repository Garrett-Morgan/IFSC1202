i = 1
maximum = 1
average = 0
sum = 0
count = 0
totalsum = 0
minimum = 10**1000000      #big number for minimum

while i != 0:
    i = int(input("Enter a Number (zero to quit): "))
    
    if i != 0:              #count
        count = count + 1
   
    if i > maximum:      #maximum
        maximum = i
    
    if i != 0:
        if i < minimum:       #minimum
            minimum = i
   
    if (i == int or float) and (i != 0):     #number of inputs
        sum = (sum + 1)

    totalsum = i + totalsum        #total sum of inputs

    average = average + i          #number of inputs for average

    
else: 
    print("Count: " + "{}".format(count))

    print("Sum: " + "{}".format(totalsum))

    print("Minimum: " + "{}".format(minimum))

    print("Maximum: " + "{}".format(maximum))

    if maximum == 0: print("Sequence length is 0") (quit())
    average = (average / sum)
    print("Average = " + "{}".format(average))