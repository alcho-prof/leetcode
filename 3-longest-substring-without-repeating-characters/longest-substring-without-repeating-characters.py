class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=set()
        i,max_len=0,0
        for j in range(len(s)):
            while s[j]  in res:
                res.remove(s[i])
                i+=1
            res.add(s[j])
            max_len=max(max_len,j-i+1)
        return max_len