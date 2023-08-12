#COding statement: 
'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''


class Solution(object):
    def searchRange(self, n, t):

        if t not in n:
            return [-1,-1]

        s =0
        e = len(n)-1
        while s<=e:
            mid = int((s+e)/2)
            if n[mid] < t:
                s = mid + 1
            else:
                e = mid - 1
            
        start = s

        s =0
        e = len(n)-1
        while s<=e:
            mid = int((s +e)/2)
            if n[mid] > t:
                e = mid - 1
            else:
                s = mid + 1

        return [start, e]
