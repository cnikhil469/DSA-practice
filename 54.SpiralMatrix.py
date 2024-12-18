class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        while(len(matrix)):
            if not len(matrix):
                return arr
            arr+=matrix[0]
            del matrix[0]
            if not len(matrix):
                return arr
            k = len(matrix)
            for i in range(k):
                arr.append(matrix[i].pop())
            k=0
            while(k<len(matrix)):
                if not len(matrix[k]):
                    del matrix[k]
                else:
                    k+=1
            if not len(matrix):
                return arr
            arr+=matrix[-1][::-1]
            del matrix[-1]
            if not len(matrix):
                return arr
            k = len(matrix)
            for i in range(k-1,-1,-1):
                arr.append(matrix[i][0])
                del matrix[i][0]
            k=0
            while(k<len(matrix)):
                if not len(matrix[k]):
                    del matrix[k]
                else:
                    k+=1
            if not len(matrix):
                return arr
