# Step 1 - Define the class object "Ball"
class House ():
# Step 2 - Define the initializer and any default values
    def __init__(self, address="", sqft=0, price=0):
# Step 3 - Define the object attributes for a ball
        self.address = address
        self.sqft = sqft
        self.price = price
# Step 4 - Define Actions (Methods) associated with the object
# Calculate Circumference for a ball
    def costpersqft(self):
        cost = self.price / self.sqft
        return cost

    def payment(self, ar, ny):
        ar = ar / 100
        ar = ar / 12
        ny = ny * 12
        payment = self.price * ( (ar * (1+ar) ** ny) / ( ( (1+ar) ** ny) -1) )
        return payment

ar = float(input("Enter Interest Rate(percent): "))    #Define percent and number of years
ny = float(input("Enter Years of Mortgage: "))

print("{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}".format("Address", "Sq Ft", "Sq Ft Cost", "Price", "Payment"))

# Step 4 - Define Actions (Methods) associated with the object
a = []

houses = open("Exam Three Houses.txt", "r")

x = houses.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = houses.readline()

houses.close()

for i in range(1):
    for j in range(1):
        house1 = House ()
        house2 = House ()
        house3 = House ()
        
        
        house1.address = str(a[0][0])
        house1.sqft = float(a[0][1])
        house1.price = float(a[0][2])

        house2.address = str(a[1][0])
        house2.sqft = float(a[1][1])
        house2.price = float(a[1][2])

        house3.address = str(a[2][0])
        house3.sqft = float(a[2][1])
        house3.price = float(a[2][2])

print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f}".format(house1.address, house1.sqft, house1.price, house1.costpersqft(), house1.payment(ar, ny)))
print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f}".format(house2.address, house2.sqft, house2.price, house2.costpersqft(), house2.payment(ar, ny)))
print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f} {:>15.2f}".format(house3.address, house3.sqft, house3.price, house3.costpersqft(), house3.payment(ar, ny)))