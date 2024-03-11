#!/bin/python
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            validParanthesis = []
            def backtrack(s, left, right):
                if len(s) == 2*n:
                    validParanthesis.append(s)
                if left < n:
                    backtrack(s+"(", left+1, right)
                if right < left:
                    backtrack(s+")", left, right+1)

            backtrack('', 0, 0)
            return validParanthesis



s = Solution()
n = 2
print(s.generateParenthesis(n))