list = str(input("Enter Values Seperated by Spaces: "))
Length = list.split()

previous = 10*100       #big number

for i in range(len(Length)):
    current = int(Length[i])
    if current > previous:
        print(current)
    previous = current