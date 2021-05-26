## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

arr_f = [0,1]

a = 0
b = 1
index = 0

while (index <= n):
    arr_f.append(a+b)
    a = b
    b = arr_f[-1]
    index = index+1
    
print(arr_f[n])
