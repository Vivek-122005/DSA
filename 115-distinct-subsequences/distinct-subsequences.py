class Solution:
    def solve(self, s: str, t: str, m: int, n:int,memo) -> int:
        if n ==0:
            return 1
        if m == 0:
            return 0
        if (m,n) in memo:
            return memo[(m,n)]
        
        if s[m-1] ==t[n-1]:
            take = self.solve(s,t,m-1,n-1,memo)
            slip = self.solve(s,t,m-1,n,memo)
            memo[(m,n)] =  take + slip
        else:
            memo[(m,n)]= self.solve(s,t,m-1,n,memo)

        return memo[(m,n)]
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        memo = {}

        return self.solve(s,t,m,n, memo)
        