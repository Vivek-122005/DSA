class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        N = len(nums)
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return[seen[needed],i]
            seen[num] = i