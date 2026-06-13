class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        total = sum(nums)
        for i in range(N):
            right = total - left - nums[i]
            if right == left:
                return i 
            left += nums[i]
        return -1            