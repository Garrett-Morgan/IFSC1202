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


for i in range(len(a)):
    for j in range(1):
        retailitem = RetailItem ()
        
        retailitem.Description = str(a[i][0])
        retailitem.UnitsOnHand = float(a[i][1])
        retailitem.Price = float(a[i][2])
        print("{:15s} {:<15.0f} {:<15.2f} {:<15.2f}".format(retailitem.Description, retailitem.UnitsOnHand, retailitem.Price, retailitem.Inventoryvalue()))        # Print the attributes
