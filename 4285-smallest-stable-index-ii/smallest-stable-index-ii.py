class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        prefix_max = nums[0]
        
        suffix_min = [0]*n
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i] = min(nums[i],suffix_min[i+1])

        for i in range(0,n):
            prefix_max = max(nums[i], prefix_max)
            if prefix_max - suffix_min[i] <= k:
                return i
        return -1
