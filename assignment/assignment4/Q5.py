def remove_duplicates(numbers):
	newlist = []
	for number in numbers:
		if number not in newlist:
			newlist.append(number)
	return newlist
print remove_duplicates([1,2,2,34,5,31,3,5,5,77,8,99,99,0,-1,-1])