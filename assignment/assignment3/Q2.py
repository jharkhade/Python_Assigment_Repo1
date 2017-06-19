class Parent():
	def print_last_name(self):
		print ("jharkhade")

class Child(Parent):
	def print_first_name(self):
		print ('Ashu')
		
ashu = Child()
ashu.print_first_name()
ashu.print_last_name()
