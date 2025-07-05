# https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    def getSecondLargest(self, arr):
        max1 = max(arr[1], arr[0])
        max2 = min(arr[1], arr[0])
        for i in arr:
            if i>max1:
                max2=max1
                max1=i
            elif i>max2 and i!=max1:
                max2=i
        return (max2 if max1!=max2 else -1)
