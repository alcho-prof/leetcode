class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        dict={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in dict.values():
                res.append(i)
            else:
                if not res or res[-1]!=dict[i]:
                    return False
                res.pop()
        return len(res)==0