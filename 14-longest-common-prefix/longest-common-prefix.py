class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        a=strs[0]
        for s in strs[1:]:
            while not s.startswith(a):
                a=a[:-1]
                if not a:
                    return ""
        return a            
