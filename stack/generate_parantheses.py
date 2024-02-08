from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        results = []

        def backtrack(cnt_openParantheses, cnt_closeParantheses):
            string = ""
            if cnt_openParantheses == cnt_closeParantheses == n:
                for s in stack:
                    string += s
                results.append(string)
                return

            if cnt_openParantheses < n:
                stack.append("(")
                backtrack(cnt_openParantheses + 1, cnt_closeParantheses)
                # this is to clean the first init of open paramtheses
                # stack.append("(")
                stack.pop() 
                
            
            # continuing the backtracking
            # this make sure the number of close parantheses is lower than open parantheses
            if cnt_closeParantheses < cnt_openParantheses:
                stack.append(")")
                backtrack(cnt_openParantheses, cnt_closeParantheses + 1)
                # this is to clean the first init of open parantheses
                # stack.append("(")
                stack.pop() 
        
        backtrack(0,0) # start from initial 0
        return results

s = Solution()
print(s.generateParenthesis(3))