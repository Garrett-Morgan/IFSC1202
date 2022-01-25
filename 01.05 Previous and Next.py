x = input( "Enter Number: ")
number = int(x)
previous = (number - 1)
next = (number + 1)
last = str(previous)
first = str(next)

print("The next number for the number " + x + " is the number " + first)
print("The previous number for the number " + x + " is the number " + last)
