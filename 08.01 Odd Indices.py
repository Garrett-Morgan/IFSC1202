def isOdd(x):
    x = int(x)
    odd = x % 2
    if odd != 0:
        return True
    else:
        return False

list = str(input("Enter Values Seperated by Spaces: "))
Length = list.split()

for i in range(len(Length)):
    odd = isOdd(i)
    if odd == True:
        print(Length[i])
