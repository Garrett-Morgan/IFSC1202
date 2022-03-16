list = str(input("Enter Values Seperated by Spaces: "))
Length = list.split()

count = 0

for i in range(len(Length)):
   if i != 0 and i != (len(Length)-1):
    current = int(Length[i])
    next = int(Length[i + 1])
    previous = int(Length[i - 1])
    if current > next and current > next:
            count += 1
print(count)