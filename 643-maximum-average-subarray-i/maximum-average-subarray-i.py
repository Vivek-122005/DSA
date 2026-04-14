class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum1 = 0
        ans = 0
        for i in range(0,k):
            sum1 += nums[i]
        ans = sum1/k
        start, end = 0, k
        while(end<n):
            sum1 -= nums[start]
            sum1 += nums[end]
            ans = max(sum1/k, ans)
            start += 1
            end += 1
        return ans

