class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start, end = 0, k
        count = 0
        for i in range(0,k):
            if s[i] in {'a', 'e', 'i', 'o','u'}:
                count += 1
        ans = count 
        while ( end< len(s)):
            if s[start] in {'a', 'e', 'i', 'o','u'}:
                count -= 1
            if s[end] in {'a', 'e', 'i', 'o','u'}:
                count +=1
            ans = max(ans, count)
            start+=1
            end +=1
        return ans

        