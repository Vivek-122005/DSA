class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        def solve(n):
            memo = [-1]* (n+1)
            if n <= 1:
                return n
            if memo[n-1] != -1:
                return memo[n-1]
            memo[n-1] = solve(n-1) + solve(n-2)
            return memo[n-1]
        return solve(n)
        