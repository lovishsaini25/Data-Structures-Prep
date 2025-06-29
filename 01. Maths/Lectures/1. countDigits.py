# https://www.geeksforgeeks.org/problems/count-digits-1606889545/1

# Approach 1 -> Recursive
def countDigits(n):
    if n==0:
        return 0
    return 1 + countDigits(n//10)


# Approach 2 -> Log function
import math
def countDigits(n):
    return math.floor(math.log(n, 10)+1)

# Approach 3 -> Itervative
def countDigits(n):
    ans = 0
    while n>0:
        ans = ans + 1
        n = n//10
    return ans
