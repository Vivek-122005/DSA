class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        currnum = 0
        currstring = ""

        for i in s:
            if i.isdigit():
                currnum = currnum *10 + int(i)
            elif i =="[":
                stack.append((currstring,currnum))
                
                currstring = ""
                currnum = 0
            elif i == "]":
                a,b = stack.pop()
                currstring = a + currstring * b
            else:
                currstring += i
        return currstring