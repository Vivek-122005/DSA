class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        data = []

        for i in range (0,N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,N):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                start = j+1
                end = N-1
                
                while start < end:
                    total = nums[i]+nums[j]+nums[start]+nums[end]
                    if total == target:
                        data.append([nums[i],nums[j],nums[start],nums[end]])
                        start +=1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start+=1
                        while start < end and nums[end] == nums[end+1]:
                            end-=1
                    elif total < target:
                        start += 1
                    else:
                        end -= 1
        return data
                