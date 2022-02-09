result = 1
x = int(input("Enter N: "))
x = x + 1       #make true range

for i in range(x):
    if i > 0: result = result * i 
    
print("{}".format(result))