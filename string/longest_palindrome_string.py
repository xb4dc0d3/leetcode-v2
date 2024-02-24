class Solution:
    def longestPalindrome(self, s: str) -> str:

        l, r = 0, 0
        currentLenString = 0
        currentLongestPalindromString = ''

        for idx in range(len(s)):
            # odd length
            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > currentLenString:
                    currentLongestPalindromString = s[l:r+1]
                    currentLenString = r - l + 1
                l -= 1
                r += 1


            # even length
            l, r = idx, idx+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > currentLenString:
                    currentLongestPalindromString = s[l:r+1]
                    currentLenString = r - l + 1
                l -= 1
                r += 1

        return currentLongestPalindromString


            




sol = Solution()
s = "babadddac"
print(sol.longestPalindrome(s))