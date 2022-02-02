x = int(input("Enter Four Digit Number: "))
ones = x % 10
threedigit = x // 10 
tens = threedigit % 10
twodigit = threedigit // 10
hundreds = twodigit % 10
onedigit = twodigit // 10
thousands = onedigit % 10
if(thousands == ones):
    if(hundreds == tens): print("YES")
else:
    print("NO")