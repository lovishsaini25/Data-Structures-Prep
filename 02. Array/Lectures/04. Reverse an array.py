# http://geeksforgeeks.org/problems/reverse-an-array/1

class Solution:
    def reverseArray(self, arr):
        low=0
        high=len(arr)-1
        while(low<high):
            arr[low], arr[high]=arr[high], arr[low]
            low+=1
            high-=1
        return arr
