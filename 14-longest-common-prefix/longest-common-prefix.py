class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        a=strs[0]
        for i in strs[1:]:
            j=0
            while j<len(a) and j<len(i) and a[j]==i[j]:
                j+=1
            a=a[:j]
            if not a:
                return ""
        return a            
