FromValue = float( input("Enter from Value: "))

FromUnit = str(input("Enter from Unit(in, ft, yd, mi): "))
if(FromUnit == "in", "ft", "yd", "mi"):
    print("Nice")
else: print("FromUnit not Valid.")

ToUnit = str(input("Enter to Unit(in, ft, yd, mi): "))
if(ToUnit != "in", "ft", "yd", "mi"):
    print("Nice")
else: print("ToUnit not Valid.")