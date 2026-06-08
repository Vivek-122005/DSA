class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        arr = []
        nums.sort()
        for i in range(N):
            start = i+1
            end = N-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    arr.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start+=1
                    while start < end and nums[end] == nums[end+1]:
                        end-=1
                    
                elif total > 0:
                    end -=1
                else:
                    start += 1
        return arr