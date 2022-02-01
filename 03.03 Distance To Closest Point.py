A = int(input("Enter Point A: "))
B = int(input("Enter Point B: "))
C = int(input("Enter Point C: "))
dist1 = B - A
dist2 = C - A
truedist1 = abs(dist1)
truedist2 = abs(dist2)
if(truedist1 < truedist2): print("{}".format(truedist1))
else:
    print("{}".format(truedist2))