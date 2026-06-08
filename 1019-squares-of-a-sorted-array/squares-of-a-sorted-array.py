class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        for i in range(N):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
        