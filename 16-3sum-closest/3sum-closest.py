class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(N):
            start = i + 1
            end = N-1
            while start < end:

                total = nums[i] + nums[start] + nums[end]
                
                if abs(total-target) < abs(closest_sum-target):
                    closest_sum = total
                if total == target:
                    return total
                if total > target:
                    end -= 1
                else:
                    start+=1
        return closest_sum