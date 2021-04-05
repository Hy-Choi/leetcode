class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for i in range(left, right+1):
            flag = True
            for sub in list(str(i)):
                if sub == '0' :
                    flag = False
                    break
                if i % int(sub) != 0 :
                    flag = False
                    break
            if flag :
                out.append(i)
        return out
                    