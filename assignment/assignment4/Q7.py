class Circle():
	def __init__(self, r):
		self.PI = 3.14
		self.radius = r
	def perimeter(self):
		return (2*self.PI*self.radius)
	def area(self):
		return (self.PI*self.radius**2)
	
calculate_Circle = Circle(6)
print (calculate_Circle.area())
print (calculate_Circle.perimeter())
	
