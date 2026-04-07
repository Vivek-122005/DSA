class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        if len(nums) == 1 :
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[e]!= nums[e-1]:
            return nums[e]
        

        while(s<=e):
            m = (s+e)//2
            print(m)
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif (m%2==0 and nums[m] == nums[m+1]) or (m%2 !=0 and nums[m] == nums[m-1]):
                s = m+1
            else:
                e = m-1
        return nums[m]

        