class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        for i  in range(0,N):
            left = 0 if i == 0 else sum(nums[0:i])
            right = 0 if i == N-1 else sum(nums[i+1:])
            if left == right:
                return i 
        return -1