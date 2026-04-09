class Solution:
    def ispossibletoeat(self, ban: int, piles: List[int], h: int) -> bool:
        temp = 0
        for i in piles:
            temp += math.ceil(i/ban)
        return temp<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles)
        res = 0
        while(min_val <= max_val):
            mid = min_val +(max_val-min_val)//2
            if self.ispossibletoeat(mid,piles,h):
                res = mid
                max_val = mid-1
                
            else:
                min_val = mid+1
        return res

        