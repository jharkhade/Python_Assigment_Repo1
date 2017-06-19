print ('!* To find the maximum nuber fro List')
def maximum_number():
	List1 = []
	n = input("How many number in your list")
	i = n
	print ('Enter list element in here :')
	while(n !=0):
		c =input()
		List1.append(c)
		n = n-1
	max = List1[0]
	

	while(n != i):
		if(max < List1[n]):
			max = List1[n]
		n = n + 1
	
	print ('Maximum Value from the list is %d' % max)
maximum_number()