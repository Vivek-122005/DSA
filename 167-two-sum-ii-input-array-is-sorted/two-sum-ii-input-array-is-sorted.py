class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        N = len(numbers)
        i,j = 0,N-1
        while(i<j):
            if numbers[i]+numbers[j] == target:
                return i+1,j+1
            elif (numbers[i]+numbers[j] < target):
                i+=1
            elif (numbers[i]+ numbers[j] > target):
                j-= 1
        return 0
        