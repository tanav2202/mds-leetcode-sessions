class Solution:
    def validation(self, ar):
        v = ["1","2","3","4","5","6","7","8","9"]
        for i in range(9):
            if ar.count(v[i]) > 1: return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for a in range(9):
            if not self.validation(board[a]): return False
        #cols
        group = ["e"]*9
        for b in range(9):
            for c in range(9):
                group[c] = board[c][b]
            if not self.validation(group): return False
        
        #boxes
        for d in range(9):
            x = (d//3)*3 # 0,0,0,3,3,3,6,6,6
            y = (d%3)*3  # 0,3,6,0,3,6,0,3,6
            for e in range(3):
                for f in range(3):
                    group[e*3+f] = board[x+e][y+f]
            if not self.validation(group): return False
        return True