class Solution:
    def wordSearch(self,arr, word) -> bool:
        hashMap = {}
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] in hashMap:
                    if i in hashMap[arr[i][j]]:
                        hashMap[arr[i][j]][i].append(j)
                    else:
                        hashMap[arr[i][j]][i] = [j]
                else:
                    hashMap[arr[i][j]] = dict()
                    hashMap[arr[i][j]][i] = [j]
       
        print(hashMap)
        if word[0] not in hashMap:
            return False

        for startRow in hashMap[word[0]]:
            for startCol in hashMap[word[0]][startRow]:
                #4 directions a word can go in
                broken = False
          
                #go right
                for i in range(startCol, startCol + len(word)):
                    if i > len(arr[0]) - 1 or arr[startRow][i] != word[i - startCol]:
                        broken = True
                        break
                if not broken:
                    return True
                broken = False
               #go down
                for i in range(startRow, startRow + len(word)):
                    if i > len(arr) - 1 or arr[i][startCol] != word[i - startRow]:
                        broken = True
                        break
                if not broken:
                    return True
        return False
'''
    Time Complxity:

        hashmap = n * m time
        in the worst case, every cell could be a potential starting point, and the word can span the max
        (n * m) * ( 2 * len(word))
        = O(w * (n * m))

    Space Complexity: 

        in the worst case, there are m*n unique characters (no repeats), which make up the keys in the hashmap. The values are all rows and columns which is (m * n) 
        So worst case time complexity is (m * n ) + (m * n) = O(m * n)
    
'''
one = Solution()
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(one.wordSearch(matrix,'FOAM'))
print(one.wordSearch(matrix,'SS'))
print(one.wordSearch(matrix,'MA'))
print(one.wordSearch(matrix,'BQP'))
print(one.wordSearch(matrix,'BQR'))
