class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        ans = 0
        start = 0
        end = len(s)
        string = set()
    
        for i in range(0,end):
            
            while s[i] in string:
                count-= 1
                string.remove(s[start])
                start+=1
                    
            count += 1
            string.add(s[i])
            ans = max(count,ans)
        return ans 



        