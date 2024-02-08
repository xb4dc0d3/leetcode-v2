from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # pair: temperature, index
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # print(results, stack)
                stack_t, stack_idx = stack.pop()
                results[stack_idx] = (idx - stack_idx)
            stack.append([t, idx])
            print(stack)
        return results

        
s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(temperatures))
            