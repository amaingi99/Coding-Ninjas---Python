def checkPalindrome(num):
	original_num = num
	rev = 0
	while(num > 0):
		rev = (10*rev)+num%10
		num = num // 10
	if (original_num == rev):
		return True
	else:
		return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
