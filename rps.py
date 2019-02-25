import random
l=["r","p","s"]
while True:
	u=input("enter n to discontinue or enter your choice  r for rock, s for scissors and p for paper ")
	if u=='n':
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses ",c)
	if u==c:
		print("tie")
	elif u=='r' and c=='s':
		print("computer wins")
	elif u=='s' and c=='r':
		print("you win")
	elif u=='r' and c=='p':
		print ("computer wins")
	elif u=='p' and c=='r':
		print("you win")
	elif u=='p' and c=='s':
		print("computer wins")
	else:
		print("you win")