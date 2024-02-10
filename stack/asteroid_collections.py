from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and asteroids[i]<0<stack[-1]:    
                if -asteroids[i]>stack[-1]:
                    stack.pop()
                    continue
                elif -asteroids[i]==stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack



# s = Solution()
# asteroids = [5,10,-20]
# print(s.asteroidCollision(asteroids))