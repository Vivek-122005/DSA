class Solution:
    def reverse(self, x: int) -> int:
        revN = 0  
        sign = -1 if x < 0 else 1  
        x = abs(x)

        
        while(x>0):
            lastdigit = x%10
            x = x//10
            revN = (revN * 10) + lastdigit
        revN = revN * sign
        
        if revN < -2**31 or revN > 2**31 - 1:
            return 0
        return revN
        