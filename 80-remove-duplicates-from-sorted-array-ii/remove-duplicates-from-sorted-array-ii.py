class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 2
        N = len(nums)
        for i in range(2,N):
            print(i)
            if nums[i] != nums[count-2] or nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count

        