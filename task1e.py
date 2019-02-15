def starts_with_vow():
	file.read() 

	file = open(“Book1.txt”, “r”) 
	x = 0
	for i in file:
   	 if i in ['a', 'e', 'i', 'o', 'u']:
       	 x += 1
print(x)
