class Solution:
    def snakesAndLadders(self, board):
        return self.helper(board, len(board) - 1, 0)



    def findLocation(self, board, number):
        number -= 1
        row = (number // len(board[0]))
        colIncrease = number % len(board[0])
        if (row % len(board) == 0: #ascending
            col = colIncrease
        else: #descending
            col = len(board[0]) - 1 - colIncrease
        return [len(board) - 1 - row, col]


    def helper(self, board, x, y): 
        visited = set()
        visited.add(1)
        queue = [[1,0]]
        while len(queue) != 0:
            val = queue.pop(0)
            location = self.findLocation(board,val[0]) 
            print(location)
            if location[0] == 0 and location[1] == len(board[0]) - 1:
                return val[1]
            else:
                for i in range(1,7):
                    newNumb = val[0] + i
                    location = self.findLocation(board, newNumb)
                    if 0 <= location[0] and 0 <= location[1] < len(board[0]): 
                        if board[location[0]][location[1]] != -1:
                            newNumb = board[location[0]][location[1]]
                        if newNumb not in visited:
                            queue.append([newNumb, val[1] + 1])
                            visited.add(newNumb)
                    
        return -1


one = Solution()
#print(one.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
#print(one.snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]))
#print(one.snakesAndLadders([[-1,4,-1],[6,2,6],[-1,3,-1]]))
#print(one.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
print(one.snakesAndLadders([[-1,-1,2,-1],[14,2,12,3],[4,9,1,11],[-1,2,1,16]]))
