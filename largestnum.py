def func(a,b,c):
	if (a>b)& (a>c):
		print("a is the largest number")
		return a
	elif (b>a) & (b>c):
		print("b is the largest number")
		return b
	else:
		print("c is the largest")
		return c
func(2,78,100)