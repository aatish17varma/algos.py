
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        beg =  0
        end = mountain_arr.length() - 1
        peak = self.findPeak(mountain_arr, beg, end)
        if mountain_arr.get(peak) == target:
            return peak
        leftIndex = self.searchLeft(mountain_arr, 0, peak, target)
        if leftIndex != -1:
            return leftIndex
        rightIndex = self.searchRight(mountain_arr, peak, mountain_arr.length() - 1, target)
        return rightIndex
        
    def findPeak(self, mountain_arr, beg, end):
        while beg <= end:
            middle = (beg + end) // 2
            middlePlusOne = mountain_arr.get(middle+1)
            if middlePlusOne > mountain_arr.get(middle):
                beg = middle + 1
            elif middlePlusOne < mountain_arr.get(middle) and mountain_arr.get(middle - 1) < mountain_arr.get(middle):
                return middle
            else:
                end = middle - 1
 
        return -1
            

    def searchLeft(self, mountain_arr, beg, end, target):
        while beg <= end:
            middle = (beg + end) // 2
            middleValue = mountain_arr.get(middle)
            if middleValue > target:
                end = middle - 1
            elif middleValue < target:
                beg = middle + 1
            else:
                return middle
        return -1
            
    def searchRight(self, mountain_arr, beg, end, target):
        while beg <= end:
            middle = (beg + end) //2
            middleValue = mountain_arr.get(middle)
            if middleValue > target:
                beg = middle +  1
            elif middleValue < target:
                end = middle - 1
            else:
                return middle 
        return -1



