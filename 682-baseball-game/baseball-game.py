class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for i in operations:
            if i not in "CD+":
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i =="D":
                s = stack[-1] *2
                stack.append(s)
            elif i =="+":
                v = stack[-1]
                q = stack[-2]
                stack.append(v+q)
        return sum(stack)
