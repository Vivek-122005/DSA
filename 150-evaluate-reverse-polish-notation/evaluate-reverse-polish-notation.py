class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','/','*']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == "+":
                    result = left + right
                elif i == "-":
                    result = left - right
                elif i == "*":
                    result = left * right
                else:
                    result = int(left / right)

                stack.append(result)
        return stack[0]