x = int(input("Enter Three Digit Number: "))
ones = x % 10
twodigit = x // 10 
tens = twodigit % 10
singledigit = twodigit // 10
hundreds = singledigit % 10
print("{}".format(ones) + "{}".format(tens) + "{}".format(hundreds))
 