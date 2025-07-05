class Solution:
    def largest(self, arr):
        return max(arr)

class Solution:
    def largest(self, arr):
        _max = arr[0]
        for i in arr:
            if _max < i:
                _max = i
        return _max
