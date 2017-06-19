class Solu:
	def Pow(self, x, n):
		if n == 0:
			return 1
		elif n ==1:
			return x
		elif n%2 == 0:
			return pow(x*x, n/2)
		else:
			return pow(x*x, n/2)*x
		
print (Solu().Pow(2,-6))
print (Solu().Pow(3,3))
print (Solu().Pow(4,2))
