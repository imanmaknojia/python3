l = ["5*1=5","5*2=10","5*3=15","5*4=20","5*5=25","5*6=30","5*7=35","5*8=40","5*9=45","5*10=50"]
for i  in range(10):
	print(l[i])
print()
l[5] = "no"

for i in range(10):
	print(l[i])