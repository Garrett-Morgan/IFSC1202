result = 0
x = int(input("Enter N: "))
for i in range(x):
    i = int(input("Enter Number: "))
    if i == 0: result = result + 1
print("{}".format(result))