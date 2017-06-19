class Person:
	def __init__(self):
		print("our class is created")
	def setFullName(self, firstName, lastName):
		self.firstName=firstName
		self.lastName=lastName
	def printFullName(self):
		print(self.firstName," ",self.lastName)

personName=Person()
personName.setFullName("Programming", "Knowledge")
personName.printFullName()
