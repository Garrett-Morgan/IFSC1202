result = 1
x = int(input("Enter Number: "))
for i in range(1, x + 1):
    result = (result * i)
print("{}".format(result))