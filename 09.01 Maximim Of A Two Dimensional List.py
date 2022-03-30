list = input("Enter the number of rows and columns: ")
list = list.split(" ")
n = int(list[0])
m = int(list[1])
a = []
max = 0

for i in range(n):
    row = (input("Enter a line of data: "))
    row = row.split(" ")
    a.append(row)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        num = int(a[i][j])
        if num > max:
            max = num


print(max)