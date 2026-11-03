class Solution:
    def solve(self, mid : int, weights: list[int], days: int) -> Boolean:
        temp = 0
        count = 1
        for i in weights:
            temp += i
            if temp > mid:
                count += 1
                temp = i
            
        return count <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        ans = 0
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right-left)//2
            if self.solve(mid,weights,days):
                ans = mid
                right = mid-1
            else:
                left = mid +1
        return ans