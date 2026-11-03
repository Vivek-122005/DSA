class Solution:

    def solve(self, mid : int ,nums: list[int], threshold: int) -> Boolean:
        total = 0
        for i in nums:
            total += math.ceil(i/mid)
        return total <= threshold


    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = 0
        while left <= right:
            mid = left + (right-left)//2
            if self.solve(mid, nums, threshold):
                ans = mid
                right = mid-1 
            else:
                left = mid +1
        return ans