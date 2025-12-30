class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start,maxLen=0,1
        for i in range(n):
            for j in range(2):
                if j == 0:
                    low, high = i, i       # odd-length
                else:
                    low, high = i, i + 1 
                
                while low>=0 and high<n and s[low]==s[high]:
                    curLen=high-low+1
                    if curLen>maxLen:
                        start=low
                        maxLen=curLen
                    low-=1
                    high+=1
        return s[start:start+maxLen]
        