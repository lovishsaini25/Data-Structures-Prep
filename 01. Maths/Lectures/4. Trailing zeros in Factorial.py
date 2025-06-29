class Solution:
    def trailingZeroes(self, n):
        result = 0
        i = 5
        while n >= i:
            result += n // i
            i *= 5
        return result
