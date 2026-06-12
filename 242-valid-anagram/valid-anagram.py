class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        see = {}
        if len(s) != len(t):
            return False
        for num in s:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        for nu in t:
            if nu not in see:
                see[nu] = 0
            see[nu] += 1
        return seen == see

            

        