def max_subarray_sum(arr):
    kandane = []
    for i in range(len(arr)):
        if len(kandane) > 0 and kandane[-1] + arr[i] > arr[i]:
            kandane.append(kandane[-1] + arr[i])
        else:
            kandane.append(arr[i])
    return max(kandane)
        

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137

