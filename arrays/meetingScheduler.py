class Solution:
    def minAvailableDuration(self,l1,l2,duration):
        first = 0
        second = 0
        l1.sort()
        l2.sort()
        while first < len(l1) and second < len(l2):
            beg = max(l1[first][0], l2[second][0])
            end = min(l1[first][1], l2[second][1])
            if beg + duration <= end:
                return [beg,beg + duration]
            else:
                if end == l1[first][1] == l2[second][1]:
                    first += 1
                    second += 1
                if l1[first][1] == end:
                    first += 1
                else:
                    second += 1
