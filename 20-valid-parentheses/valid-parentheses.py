class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=="[" or s[i]=="{":
                a.append(s[i]) 
            else:
                if a and((a[-1]=='(' and s[i]==')') or (a[-1]=='[' and s[i]==']') or (a[-1]=='{' and s[i]=='}')):
                    a.pop()

                else:
                    return False
        return not a                   