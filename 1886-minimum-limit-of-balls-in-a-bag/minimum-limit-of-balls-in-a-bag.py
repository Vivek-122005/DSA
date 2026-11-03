class Solution:
    def solve (self, mid:int, nums: list[int], maxOperations: int) -> int:
        temp = 0
        for i in nums:
            if i <= mid:
                continue 
            temp += math.ceil(i/mid) -1
        return temp <= maxOperations
        


    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        ans = 0
        min_val = 1
        max_val = max(nums)

        while min_val <= max_val:
            mid = min_val + (max_val-min_val)//2
            if self.solve(mid,nums,maxOperations):
                ans = mid
                max_val = mid -1
            else:
                min_val = mid +1
        return ans