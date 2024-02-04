class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0
        longest = 0
        used_char = {} # dictionary of string
        
        for i in range(n):
            if (s[i] in used_char and start <= used_char[s[i]]):
                start = used_char[s[i]] + 1
            else:
                 longest = max(longest , i-start +1)
            used_char[s[i]] = i
        return longest
    
# s = Solution()
# string = "pwwkew"
# print(s.lengthOfLongestSubstring(string))