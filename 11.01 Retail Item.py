# Step 1 - Define the class object "Ball"
class RetailItem ():
	
# Step 2 - Define the initializer and any default values

    def __init__(self, Description="", UnitsOnHand=0, Price=0):

# Step 3 - Define the object attributes

        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price

# Step 4 - Here is another action
    def Inventoryvalue(self): 
        inventoryvalue =  self.UnitsOnHand * self.Price
        return inventoryvalue


print("{:15s} {:15s} {:15s} {:15s}".format("Description", "Units on Hand", "Price", "Inventory Value"))

# Step 4 - Define Actions (Methods) associated with the object
a = []

inventory = open("10.02 Inventory.txt", "r")

x = inventory.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = inventory.readline()

inventory.close()


for i in range(len(a)):
    for j in range(1):
        retailitem1 = RetailItem ()
        retailitem2 = RetailItem ()
        retailitem3 = RetailItem ()
        
        retailitem1.Description = str(a[0][0])
        retailitem1.UnitsOnHand = float(a[0][1])
        retailitem1.Price = float(a[0][2])

        retailitem2.Description = str(a[1][0])
        retailitem2.UnitsOnHand = float(a[1][1])
        retailitem2.Price = float(a[1][2])

        retailitem3.Description = str(a[2][0])
        retailitem3.UnitsOnHand = float(a[2][1])
        retailitem3.Price = float(a[2][2])
        
print("{:15s} {:<15.0f} {:<15.2f} {:<15.2f}".format(retailitem1.Description, retailitem1.UnitsOnHand, retailitem1.Price, retailitem1.Inventoryvalue()))        # Print the attributes
print("{:15s} {:<15.0f} {:<15.2f} {:<15.2f}".format(retailitem2.Description, retailitem2.UnitsOnHand, retailitem2.Price, retailitem2.Inventoryvalue()))        # Print the attributes
print("{:15s} {:<15.0f} {:<15.2f} {:<15.2f}".format(retailitem3.Description, retailitem3.UnitsOnHand, retailitem3.Price, retailitem3.Inventoryvalue()))        # Print the attributes

# Read a file and append the vales to the ball list
def add_ball_from_file(self, InventoryUpdate):
	update = open(InventoryUpdate.txt)
	x = update.readline()
	while x != "":
#			print(x) # display what was read
		y = x.split(",")
#			print(y) # display the result of the split
		self.price(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
		x = ballfile.readline()
	update.close()
