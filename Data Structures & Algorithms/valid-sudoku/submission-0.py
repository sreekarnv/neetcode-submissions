class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue
                
                curr = board[row][col]
                boxId = (row // 3, col // 3)

                if curr in rows[row] or curr in cols[col] or curr in boxes[boxId]:
                    return False
                
                rows[row].add(curr)
                cols[col].add(curr)
                boxes[boxId].add(curr)
        
        return True