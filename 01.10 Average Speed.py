miles = int(input("Enter Length of Race in Kilometers: ")) / 1.61
min = int(input("Enter Minutes: ")) / 60
sec = int(input("Enter Seconds: ")) / 3600
hours = min + sec
MPH = miles / hours
speed = str(MPH)
print(speed)
