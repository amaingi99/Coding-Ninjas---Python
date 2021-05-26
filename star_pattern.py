## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <=n:
    spaces = 1
    while spaces <=n-i:
        print(" ", end='')
        spaces = spaces + 1
    
    stars = 1
    while stars <= i:
        print("*", end='')
        stars = stars + 1
        
    num = i-1
    while num >=1:
        print("*", end = '')
        num = num - 1
    
    print()
    i = i + 1
