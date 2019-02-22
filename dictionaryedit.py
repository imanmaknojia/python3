
import random

d={8:37,11:2,13:34,28:4,38:9,40:68,50:34,48:27}


p= random.choice([2,8,11,28,40,59,48])

print("you got",p)

if p in d:
	if p> d[p]:
		print("snake")
	else:
		print("ladder")

	print("you can go to",d[p])