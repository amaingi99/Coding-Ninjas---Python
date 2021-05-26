## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
	p = n-i+1
	k = 1
	while k<=i:
		charP = chr(ord('A')+p-1)
		print(charP, end='')
		p = p+1
		k = k+1	
	print()
	i = i+1
