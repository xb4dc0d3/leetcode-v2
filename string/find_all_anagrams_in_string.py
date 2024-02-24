from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        array_indices = []
        sorted_p = ''.join(sorted(p))
        idx = 0
        window_string = ''

        for c in s:
            window_string += c
            if len(window_string) == len(p):
                sorted_s = ''.join(sorted(window_string))
                if sorted_s == sorted_p:
                    array_indices.append(idx)
                window_string = window_string[1:]
                idx += 1
    
        return array_indices