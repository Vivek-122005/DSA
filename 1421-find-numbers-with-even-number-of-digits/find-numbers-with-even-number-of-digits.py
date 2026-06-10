class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digit = 0
            x = i
            while x:
                digit+=1
                x= x //10
            if digit %2 == 0:
                count+= 1
        return count
        