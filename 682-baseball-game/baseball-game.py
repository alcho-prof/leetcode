class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i=="C":
                res.pop()
            elif i=="D":
                res.append(2*res[-1])
            elif i=="+":
                res.append(res[-1]+res[-2])
            else:
                res.append(int(i))
        return sum(res)                    