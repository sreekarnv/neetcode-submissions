class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] == ".":
                    continue
                
                current = board[row][col]
                rc = (row // 3, col // 3)

                if current in rows[row] or current in cols[col] or current in boxes[rc]:
                    return False
                
                rows[row].add(current)
                cols[col].add(current)
                boxes[rc].add(current)

        return True