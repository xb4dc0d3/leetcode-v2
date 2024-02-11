class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result = {}
        maxFreq = 0
        lp = 0 # left pointer
        rp = 0 # right pointer
        max_len = -999999999
        for rp, char in enumerate(s):
            result[char] = result.get(char,0) + 1
            maxFreq = max(maxFreq, result[char])
            
            if (rp-lp+1) - maxFreq > k:
                result[s[lp]] -= 1
                lp += 1

            max_len = max(max_len, rp-lp+1)

        return max_len
