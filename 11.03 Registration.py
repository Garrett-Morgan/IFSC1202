# Step 1 - Define the class object "Ball"
class Student ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, firstname="", lastname="", tnumber=0):

# Step 3 - Define the object attributes
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.courselist = []

# Step 1 - Define the class object "Ball"
class StudentList ():
# Step 2 - Define the initializer and any default values
	def __init__(self):
# Step 3 - Define the object attributes for a ball
		self.studentlist = []
# Step 4 - Define Actions (Methods) associated with the object
    def add_student(self, firstname, lastname, tnumber):

    def find_student(self, studenttofind):

    def print_student_list(self):

    def add_student_from_file(self, filename):