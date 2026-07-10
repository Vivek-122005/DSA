class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currnum = 0
        prev = "+"
        for i, ch in enumerate(s):
            # if ch == " ":
            #     continue
            if ch.isdigit():
                currnum = currnum*10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == len(s)-1:
                if prev == "+":
                    stack.append(currnum)
                elif prev =="-":
                    stack.append(-currnum)
                elif prev =="*":
                    stack.append(stack.pop()*currnum)
                else:
                    stack.append(int(stack.pop()/currnum))
                currnum = 0
                prev = ch
        return sum(stack)        