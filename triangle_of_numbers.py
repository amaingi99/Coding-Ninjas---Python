## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1

while i<=n:
    spaces = 1
    while spaces <=n-i:
        print(' ', end='')
        spaces = spaces+1
    
    j=1
    p = i
    while j <= i:
        print(p,end='')
        p = p+1
        j = j+1
        
    k = p-2
    while k >=i:
        print(k,end='')
        k = k-1
        
    print()
    i = i+1
