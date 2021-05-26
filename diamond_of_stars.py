## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i=1

while i<=(n+1)/2:
    spaces = 1
    while spaces <=(n+1)/2-i:
        print(' ',end='')
        spaces = spaces +1
    
    stars = 1
    while stars <=i:
        print("*",end='')
        stars = stars + 1
    
    p = i-1
    while p>=1:
        print("*", end='')
        p = p-1
        
    print()
    i = i+1

i=1

while i<=n/2:
    spaces = 1
    while spaces <= i:
        print(' ',end='')
        spaces = spaces+1
    stars = 1
    while stars <= (n/2 -i +1):
        print("*",end='')
        stars = stars+1
    
    p = n/2-i
    while p >=1:
        print("*",end='')
        p = p-1
        
    print()
    i = i+1
