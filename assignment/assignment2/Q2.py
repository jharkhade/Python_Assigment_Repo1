num1 = input("enter the first number")
num2 = input("enter the second number")
num3 = input("enter the third number")
if num1>=num2 and num1>=num3:
    print "greatest number is:", num1
elif num2>=num1 and num2>=num3:
    print "greatest number is", num2
else:
    print "greatest number is", num3