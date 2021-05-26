## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i <=n:
	p = i
	j = 1
	while j <= i:
		print(p,end='')
		p = p-1
		j = j+1
	print()
	i = i+1
