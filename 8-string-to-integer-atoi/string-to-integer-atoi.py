class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        if s[0] in ["-","+"]:
            if s[0]=="-":
                sign=-1
            s=s[1:]
        res=0
        for i in s:
            if i.isdigit():
                res=res*10+int(i)
            else:
                break
        res*=sign

        m,n=-2**31,2**31-1
        if res<m:
            return m
        if res>n:
            return n
        return res


            