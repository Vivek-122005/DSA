class Solution:
    def check(self,mid: int, n: int, quantities: List[int]) -> bool:
        temp = 0
        for i in quantities:
            temp += math.ceil(i/mid)
        return temp <= n

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        min_val, max_val = 1, max(quantities)
        res = 0
        if n == len(quantities):
            return max(quantities)
        
        while(min_val <= max_val):
            mid = min_val + (max_val-min_val)//2
            if self.check(mid, n, quantities ):
                res = mid
                max_val = mid-1
            else:
                min_val = mid+1
        return res           
        