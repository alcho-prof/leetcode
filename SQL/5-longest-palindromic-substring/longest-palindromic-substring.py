class Solution:
    def longestPalindrome(self, s: str) -> str:
        start,maxlen=0,1
        for i in range(len(s)):
            for j in range(2):
                if j==0:
                    low,high=i,i
                else:
                    low,high=i,i+1
                while low>=0 and high<len(s) and s[low]==s[high]:
                    curlen=high-low+1
                    if curlen>maxlen:
                        start=low
                        maxlen=curlen
                    low-=1
                    high+=1
        return s[start:maxlen+start]