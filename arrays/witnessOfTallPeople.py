def witnesses(heights):
    answer =0 
    maxHeight = float('-inf')
    for i in range(len(heights) - 1, -1,-1):
        if heights[i] > maxHeight:
            answer += 1
        maxHeight = max(maxHeight, heights[i])
    return answer        

print(witnesses([3, 6, 3, 4, 1]))
