class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0,len(nums)-1
        listt = [-1,-1]
        while left <= right:
            mid= left + (right-left)//2

            if nums[mid] == target:
                
                listt[0] = mid
                right = mid -1
            elif nums[mid] < target:
                left = mid+1
            else:
                right =  mid-1

                
        left, right = 0,len(nums)-1
        while left <= right:
            mid= left + (right-left)//2

            if nums[mid] == target:
                
                listt[1] = mid
                left = mid +1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid -1
        return listt