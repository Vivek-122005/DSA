class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        count = 0
        ans = 1000000000
        for i in range(end):
            count += nums[i]
            while count >= target:
                ans = min(i-start+1,ans)
                count -= nums[start]
                start+=1
        
        return 0 if ans == 1000000000 else ans
            

        


