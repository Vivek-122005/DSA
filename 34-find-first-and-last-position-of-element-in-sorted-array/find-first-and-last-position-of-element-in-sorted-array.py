class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = [-1,-1]
        lst[0]= self.first(nums, target)
        lst[1]= self.last(nums, target)
        return lst

    def first(self,nums, target):
        ans = -1
        s = 0
        e = len(nums)-1
        while(s<=e):
            m = (e+s)//2
            if (target<nums[m]):
                e = m-1
            elif (target > nums[m]):
                s = m+1
            else:
                ans = m
                e = m-1
        print("first",ans)
        return ans

    def last(self,nums, target):
        ans = -1
        s = 0
        e = len(nums)-1
        while(s<=e):
            m = (e+s)//2
            if (target<nums[m]):
                e = m-1
            elif (target > nums[m]):
                s = m+1
            else:
                ans = m
                s = m+1
        return ans 

            