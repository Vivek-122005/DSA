class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack= []
        for i in asteroids:
            while stack and i < 0 and stack[-1] >0:
                if stack[-1] == abs(i):
                    stack.pop()
                    break
                elif stack[-1] < abs(i):
                    stack.pop()
                else:
                    break
            else:
                stack.append(i)
        return stack          

            

            

            
            
            



                

        