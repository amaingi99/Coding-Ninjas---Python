## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
num = int(input())
sum_even = 0
sum_odd = 0

while (num >0):
    if (num%10)%2 == 0:
        sum_even = sum_even + (num%10)
    else:
        sum_odd = sum_odd + (num%10)
        
    num = num // 10
    
print(sum_even, sum_odd)
