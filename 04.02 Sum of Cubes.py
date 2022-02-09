result = 0
x = int(input("Enter N: "))
x = x + 1       #make true range

for i in range(x):
    result = result + (i ** 3) 
    
print("{}".format(result))