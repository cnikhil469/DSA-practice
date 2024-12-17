class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matLen = len(matrix)-1
        aloha=[]
        for j in range(0, matLen+1):
            a = matrix[j]
            d = []
            for k in range(matLen, -1, -1):
                d.append(matrix[k][j])
            aloha.append(d)
        for i in range(len(aloha)):
            matrix[i] = aloha[i]
