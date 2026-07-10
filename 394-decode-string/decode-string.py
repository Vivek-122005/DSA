class Solution:
    def decodeString(self, s: str) -> str:
        countstack = []
        stringstack =[]
        currnum = 0
        currstring = ""

        for i in s:
            if i.isdigit():
                currnum = currnum *10 + int(i)
            elif i =="[":
                countstack.append(currnum)
                stringstack.append(currstring)
                currstring = ""
                currnum = 0
            elif i == "]":
                a = countstack.pop()
                b = stringstack.pop()
                currstring = b + currstring * a
            else:
                currstring += i
        return currstring