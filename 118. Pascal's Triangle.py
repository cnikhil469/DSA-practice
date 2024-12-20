class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = numRows
        if r==1:
            return [[1]]
        if r==2:
            return [[1], [1,1]]
        else:
            res = [[1], [1,1]]
            f = r-2
            while(f):
                k=[]
                m,i = res[-1],0
                while(i<len(m)-1):
                    k.append(sum(m[i:i+2]))
                    i+=1
                res.append([1]+k+[1])
                f-=1
            return res


        
