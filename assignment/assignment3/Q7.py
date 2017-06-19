class Parent():
	def __init__(self):
		self.s =""

	def getString(self):
		self.s = raw_input()

	def printString(self):
		print self.s.upper()


class Child(Parent):
	print ("Enter your String here")

strObj = Child()
strObj.getString()
strObj.printString()