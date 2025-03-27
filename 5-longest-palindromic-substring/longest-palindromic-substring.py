class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = 0  # Track the longest palindrome length
        
        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > n:
                    res = s[l:r+1]
                    n = r - l + 1
                l -= 1
                r += 1

            # Even-length palindrome (centered between i and i+1)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > n:
                    res = s[l:r+1]
                    n = r - l + 1
                l -= 1
                r += 1

        return res

