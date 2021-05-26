# Write your code here
while(True):
	ip = int(input())
	if ip == 6:
		exit()

	else:
		if ip >= 1 and ip <= 5: 
			a = int(input())
			b = int(input())
			if ip == 1:
				print(a+b)
			elif ip == 2:
				print(a-b)
			elif ip == 3:
				print(a*b)
			elif ip == 4:
				print(a//b)
			elif ip == 5:
				print(a%b)
		else:
			print("Invalid Operation")
