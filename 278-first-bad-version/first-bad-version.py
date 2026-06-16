# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0 
        end = n
        res = 0
        while start <= end:
            mid = start + (end-start)//2
            if isBadVersion(mid) == True:
                res = mid
                end = mid -1
            else:
                start = mid +1
        return res
        