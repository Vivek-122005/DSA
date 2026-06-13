class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]*N
        suffix = [0]*N        
        for i  in range(1,N):
            prefix[i] = prefix[i-1]+nums[i-1]
        for i in range(N-2,-1,-1):
            suffix[i] = suffix[i+1]+ nums[i+1]
        print(prefix)
        print(suffix)
        for i in range(N):
            if suffix[i] == prefix[i]:
                return i
        return -1

