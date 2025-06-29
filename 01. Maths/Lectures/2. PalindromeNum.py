# https://www.geeksforgeeks.org/problems/palindrome0746/1

class Solution:
    def isPalindrome(self, n):
        rev = 0
        org_num = n
        while n > 0:
            rev = rev * 10 + (n%10)
            n = n //10
        return rev == org_num
