x = int(input("Enter Number: "))
for i in range(0, x+1):
    print("{}".format(i) + "*" + "{}".format(i) + "=")
    print(i*i)