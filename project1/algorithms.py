#Algorithm 1
def enum_msa(array=[]):
    maxSum = 0
    startIdx = 0
    stopIdx = 0

    for i in range(0, len(array)):
        curStart = i
        for j in range(i, len(array)):
            cur = 0
            for k in range(i, j + 1):
                cur += array[k]
                if cur > maxSum:
                    maxSum = cur
                    startIdx = i
                    stopIdx = j

    return startIdx, stopIdx, maxSum

#Algorithm 2
def betterEnum_msa(array=[]):
    maxSum = 0
    startIdx = 0
    stopIdx = 0
    for i in range(0, len(array)):
        cur = 0
        for j in range(i, len(array)):
            cur += array[j]
            if cur > maxSum:
                maxSum = cur
                startIdx = i
                stopIdx = j
    return startIdx, stopIdx, maxSum

#Algorithm 4
def linearTime_msa(array=[]):
    max_so_far = array[0]
    max_ending_here = 0
    start_idx, stop_idx, start_idx_so_far = 0    #Initial maximum subarray is array[0:0]

    for i in (1, len(array)):
        if(max_ending_here + array[i] > array[i]):  #should this be gt or gteq?
            max_ending_here += array[i]
        else:
            max_ending_here = array[i]
            start_idx_so_far = i

        if(max_so_far < max_ending_here):   #should this be lt or lteq?
            max_so_far = max_ending_here
            start_idx = start_idx_so_far
            stop_idx = i

    return max_so_far
