class Solution:
    
    '''
        Time Complexity: (board width * board length) * 3^(length of the word)

            Reasoning: We can start our search on any place of the board (width * length), and for each place, we recursively search the board. For example, we start in the middle of the board and move in 3 directions (the first letter check will be 4 directions, but we will check three after (sometimes less), because we will be going backwards (aka reusing the same letter (not allowed)). The depth of our search will never surpass the length of the word. 

        Space Complexity: length of the word 
            Reasoning: We will be recursively searching the tree, so the space complexity is determined by the max length of the call stack which is the lenght of the word


    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.helper(board, word[1 : ], i, j):
                        return True
                    
        return False
    
    
    def helper(self, board, word, x, y):
        if len(word) == 0:
            return True
        
        answer = False
        oldVal = board[x][y]
        board[x][y] = '#'
        
        if x + 1 < len(board) and board[x+1][y] == word[0]:
            answer |= self.helper(board, word[1 : ], x+1, y)
            if answer:
                return True
        
        if x - 1 >= 0 and board[x-1][y] == word[0]:
            answer |= self.helper(board, word[1 : ], x-1, y)
            if answer:
                return True

        if y + 1 < len(board[0]) and board[x][y+1] == word[0]:
            answer |= self.helper(board, word[1 : ], x, y+1)
            if answer:
                return True
        if y - 1 >= 0 and board[x][y-1] == word[0]:
            answer |= self.helper(board, word[1 : ], x, y-1 )
            if answer:
                return True
            
        board[x][y] = oldVal
        return answer
    
    
