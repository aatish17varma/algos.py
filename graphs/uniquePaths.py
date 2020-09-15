'''
    Find the number of unique paths to the bottom right element in an n*m grid array
'''

class Solution:
    def uniquePaths(m,n):
        paths = [[0 for i in range(m)] for i in range(n)] 
        paths[0][0] = 1 
        for i in range(len(paths)):
            for j in range(len(paths[0])):
                if j-1 >= 0:
                    paths[i][j] += paths[i][j-1]
                if i-1 >= 0:
                    paths[i][j] += paths[i-1][j]

        return paths[-1][-1]


print(Solution.uniquePaths(3,2))
print(Solution.uniquePaths(7,3))
