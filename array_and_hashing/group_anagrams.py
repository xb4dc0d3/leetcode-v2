from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            new_word = ''.join(sorted(word)) # this is the sorted word and will be used as lookup key
            if new_word in results.keys():
                results[new_word] += [word]
            else:
                results[new_word] = [word]
        return [res for res in results.values()]


# strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# s = Solution()
# print(s.groupAnagrams(strs))