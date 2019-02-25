import random
l=["r","p","s"]
u=input("enter your choice ")
c=random.choice(l)
print("computer chooses",c)
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