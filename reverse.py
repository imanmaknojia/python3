name= input("enter the name you want to reverse: ")
def reverse(name):
	string=" "
	for i in name:
		string= i+string
	return string
print("the reversed name is")
print(reverse(name))
reverse(name)

