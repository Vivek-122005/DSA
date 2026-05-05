class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n = len(board)
        m = len(board[0])

        def check(r,c,k):
            if k == len(word):
                return True
            if not (0 <= r < n) or not (0 <= c < m) or (r,c) in visited  or board[r][c] != word[k]:
                return False
            
            visited.add((r,c))
            res = check(r+1, c, k+1) or check(r-1, c, k+1) or check(r, c+1, k+1) or check(r, c-1, k+1)
            visited.remove((r,c))
            return res

        for i in range(n):
            for j in range(m):
                if check(i,j,0):
                    return True
        return False
