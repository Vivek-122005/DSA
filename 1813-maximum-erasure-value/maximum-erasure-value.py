class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        ans = 0
        count = 0
        store = set()
        for i in range(end):
    
            while nums[i] in store:
                store.remove(nums[start])
                count-= nums[start]
                start += 1

            count += nums[i]
            store.add(nums[i])
            ans = max(count, ans)
        return ans



        