
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            pos[num].append(i)
            if len(pos[num])>1:
                return True
        return False    
        