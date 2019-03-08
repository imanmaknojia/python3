import random
l=["r","p","s"]
d={"r":"rock", "s":"scissors","p":"paper"}
cs=0
us=0
while True:
	u=input("enter n to discontinue or enter your choice  r for rock, s for scissors and p for paper: ")
	if u=='n':
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses ",d[c])
	print("user choses ",d[u])
	if u==c:
		print("tie")
	elif u=='s' and c=='p':
		print("you win")
		us=us+1
	elif u=='p' and c=='r':
		print("you win")
		us=us+1
	elif u=='r' and c=='s':
		print("you win")
		us=us+1
	else:
		print("computer wins")
		cs=cs+1
	print("your score is ",us,"and the computers score is ",cs )
	print()
	if us==5:
		print("user wins this round")
		exit()
	elif c==5:
		print("computer won this round")
		exit()

 