class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        while i <= len(nums) and j <= len(nums):
            if nums[i] + nums[j] == target :
                return i, j
                break
            else :
                if j == len(nums)-1 :
                    i += 1
                    j = i+1
                else :
                    j += 1
