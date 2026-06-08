class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        result = []
        for i in nums:
            result.append(i*i)
        result.sort()
        return result
        