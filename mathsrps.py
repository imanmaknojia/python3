import random
l=["r","p","s"]
us=0
cs=0
while True:
	u=input("enter n to discontinue or enter your choice  r for rock, s for scissors and p for paper ")
	if u=='n':
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses ",c)
	s=l.index(c)
	a=l.index(u)
	if u==c:
		print("tie")
	elif (s+1)%3==a:
		print("user wins")
		us=us+1
	else:
		print("computer wins")
		cs=cs+1
	print("users score: ", us, "computers score is: ", cs)
	if us==5:
		print("user wins this rounds")
		exit()
	elif cs==5:
		print("computer wins this round")
		exit()	
		


	