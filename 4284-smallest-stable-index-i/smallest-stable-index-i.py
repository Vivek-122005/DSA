class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0
        for i in range(n):
            stable_max = max(nums[:i+1])
            stable_min = min(nums[i:])
            stable = stable_max - stable_min
            if stable <= k:
                return i
        return -1



        