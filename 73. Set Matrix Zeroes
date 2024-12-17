class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indArr = []
        for i in range(len(matrix)):
            k=0
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    k=1
                    indArr.append(j)
            if k:
                matrix[i] = [0]*len(matrix[i])
        indArr = set(indArr)
        while(len(indArr) > 0):
            ele = indArr.pop()
            for i in range(len(matrix)):
                matrix[i][ele] = 0


            
        
