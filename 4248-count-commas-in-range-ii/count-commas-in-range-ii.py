class Solution:
    def countCommas(self, n: int) -> int:
        power = 1000
        count = 0
        while power <=n:
            count += n - power + 1
            power *= 1000
        return count
        