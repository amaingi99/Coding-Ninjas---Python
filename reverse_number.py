def reverse(n):
    reverse = 0
    while (n > 0):
        reverse = (10*reverse) + (n%10)
        n = n//10
    return reverse

n=int(input())
result = reverse(n)
print(result)
