list = str(input("Enter Values Seperated by Spaces: "))
Length = list.split()

y = (max(Length))
x = (Length.index(max(Length)))

print("Largest Value: {}".format(y))
print("Index of Largest Value: {}".format(x))