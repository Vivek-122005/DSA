class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sumarr = {}
        running_sum = 0
        ans = 0
        for i in range(0,n):
            running_sum += nums[i]
            if running_sum ==k:
                ans +=1
            
            if running_sum - k in sumarr:
                ans += sumarr[running_sum-k]
            
            if running_sum in sumarr:
                sumarr[running_sum] += 1
            else:
                sumarr[running_sum] = 1
            
        return ans
        