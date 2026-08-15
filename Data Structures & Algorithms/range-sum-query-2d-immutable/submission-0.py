class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.m = []
        
        for r in range(rows + 1):
            arr = []
            for c in range(cols + 1):
                arr.append(0)
            self.m.append(arr)
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                top = self.m[r][c + 1]
                self.m[r + 1][c + 1] = prefix + top


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.m[row2][col2]
        top_left = self.m[row1 - 1][col1 - 1]
        top_right = self.m[row1 - 1][col2]
        bottom_left = self.m[row2][col1 - 1]

        return bottom_right + top_left - top_right - bottom_left




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)