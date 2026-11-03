class Solution:

    def solve(self, mid:int,pos: list[int],m:int) -> Boolean:
        countball = 1
        rightnow = pos[0]
        for i in pos:
            if i-rightnow >= mid:
                countball +=1
                rightnow = i
        return countball >= m

    def maxDistance(self, pos: list[int], m: int) -> int:
        pos = sorted(pos)
        ans = 0
        left = 1
        right = pos[-1]-pos[0]
        while left <= right:
            mid = left + (right-left)//2
            if self.solve(mid,pos,m):
                ans = mid
                left = mid +1
            else:
                right = mid-1
        return ans