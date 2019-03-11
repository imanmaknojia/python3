try:
	a=int(input("give a number "))
	if a<=3:
		s=float((a/a-3))
		print(s)
	
except(NameError,ZeroDivisionError):
	print("SyntaxError")
	