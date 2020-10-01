class Solution:
    def tictactoe(self, moves):
            
        def helper(board,position):
            #eightPossibilities
            if board[0][0] == board[0][1] == board[0][2] == position:
                return True 
            if board[1][0] == board[1][1] == board[1][2]== position:
                return True

            if board[2][0] == board[2][1] == board[2][2] == position:
                return True

            if board[0][0] == board[1][0] == board[2][0] == position:
                return True
            
            if board[0][1] == board[1][1] == board[2][1] == position:
                return True

            if board[0][2] == board[1][2] == board[2][2] == position:
                return True 

            if board[0][0] == board[1][1] == board[2][2] == position:
                return True

            if board[0][2] == board[1][1] == board[2][0] == position:
                return True

            return False

        board = [[None for _ in range(3)] for _ in range(3)] 
        for move in range(len(moves)):
            board[moves[move][0]][moves[move][1]] = 'A' if move % 2 == 0 else 'B' 

        aAnswer = helper(board,'A')
        bAnswer = helper(board,'B')
        if aAnswer:
            return 'A'
        elif bAnswer:
            return "B"
        elif len(board) == 9:
            return "Draw"
        else:
            return "Pending"


one = Solution()
print(one.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
