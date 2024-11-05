def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num
def check_palindrome(n):
    reverse_num = reverse_number(n)
    if (n==reverse_num):
        print (True)
        return True
    elif(n!=reverse_num):
        return False
class Solution(object):
    def isPalindrome(self, x):
       return check_palindrome(x)
        
