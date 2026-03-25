class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        print(n)
        revN = 0
        x = abs(x)
        
        while x>0:
            lastdigit = x % 10
            x = x//10
            revN = (revN*10)+ lastdigit
        
        print(revN)
        if revN == n:
            return True
        
        else:
            return False
        