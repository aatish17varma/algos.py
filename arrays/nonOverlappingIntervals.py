class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])
        intervals = sorted(intervals, key = lambda x : x[0])
        # if there are two intervals that start at the same time, then the one that ends first appears before
        toBeRemoved = 0
        indicesOfRemoved = set()
        i = 0
        j = 1
        while i < len(intervals) and j < len(intervals):
            if i in indicesOfRemoved:
                i += 1
            elif j in indicesOfRemoved:
                j += 1
            elif intervals[i][0] == intervals[j][0]: # e.g. [0, 3], [0,4] (makes sense to remove the second)
                toBeRemoved += 1
                indicesOfRemoved.add(j)
                j += 1
            elif intervals[j][0] < intervals[i][1]:
                if intervals[j][1] <= intervals[i][1]:
                    #remove i 
                    toBeRemoved += 1
                    indicesOfRemoved.add(i)
                    i = j # we move i to j because we have already handled all the cases between i and j
                    j += 1
                else: #remove j because it ends later 
                    #remove j
                    toBeRemoved += 1
                    indicesOfRemoved.add(j)
                    j += 1
            else:
                i = j 
                j = i + 1
            
        return toBeRemoved

one = Solution()
print(one.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(one.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(one.eraseOverlapIntervals([[1,2],[2,3]]))
