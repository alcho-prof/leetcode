class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        res=0
        prev=0
        for i in reversed(s):
            a=dic[i]
            if a<prev:
                res-=a
            else:
                res+=a
            prev=a
        return res