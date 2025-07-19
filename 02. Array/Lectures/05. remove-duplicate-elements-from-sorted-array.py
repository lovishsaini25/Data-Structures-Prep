# https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
# Time, space complexity:
class Solution:
    def removeDuplicates(self, arr):
        result = []
        result.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i]>arr[i-1]:
                result.append(arr[i])
        return result

# Issue
# What if we delete the index and then, we read it again in the next interation and i-1 (during next iter) will cause issue
class Solution:
    def removeDuplicates(self, arr):
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1]:
                del arr[i]
        return arr


# Best solution
class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []
        write = 1
        for read in range(1, len(arr)):
            if arr[read] != arr[read - 1]:
                arr[write] = arr[read]
                write += 1
        return arr[:write]