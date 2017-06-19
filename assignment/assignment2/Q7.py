def IsLeapYear(year):
	if((year % 4) == 0 ):
		if ((year % 100) == 0):
			if((year % 400) == 0):
				return 1
			else:
				return 0
		else:
			return 1
	return 0

n = 20016
print "program to check the leap year"
print " Enter the year:"
#n = input()
if (IsLeapYear(n) == 1):
	print n, " is a leap year"
else:
	print n, "is not a leap year"
	