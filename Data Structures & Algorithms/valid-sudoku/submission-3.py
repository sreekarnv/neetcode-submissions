class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue
                
                val = board[r][c]

                boxIdx = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[boxIdx]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[boxIdx].add(val)
        
        return True