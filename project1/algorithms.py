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

#Algorithm 3
def recursive_msa(left_bound, right_bound, array=[]):
    left_max, mid_max, right_max, sub_max, total_sum = 0
    max_left_side, max_right_side = -1000000, -1000000
    
    #Check if the is only one variable left
    if (left_bound == right_bound):
        return array[left_bound]
    
    #Find the maximum subarrays on the left and right
    left_max = recursive_msa(left_bound,(left_bound+right_bound)/2, array)
    right_max = recursive_msa((left_bound+right_bound)/2+1,right_bound, array)
    
    #Maximum for a middle sub array array
    #Find max on left side
    for i in range((left_bound+right_bound)/2, left_bound-1, -1):
        total_sum += array[i]
        #Update the left side maximum
        if (total_sum > max_left_side):
            max_left_side = total_sum
    total_sum = 0
    #Find max on right side
    for i in range((left_bound+right_bound)/2+1,right_bound+1):
        total_sum += array[i]
        #Update the right side maximum
        if (total_sum > max_right_side):
            max_right_side = total_sum
    
    mid_max = max_left_side + max_right_side

    #Finds the biggest of the three and returns it
    sub_max = max(max(left_max,right_max),mid_max)
    
    return sub_max

def recursive_holder_msa(array=[]):
    max = recursive_msa(0,len(array), array)
    return max


#Algorithm 4
def linearTime_msa(array=[]):
    max_so_far = array[0]
    max_ending_here = 0
    start_idx = 0
    stop_idx = 0
    start_idx_so_far = 0    #Initial maximum subarray is array[0:0]

    for i in range(1, len(array)):
        if(max_ending_here + array[i] > array[i]):  #should this be gt or gteq?
            max_ending_here += array[i]
        else:
            max_ending_here = array[i]
            start_idx_so_far = i

        if(max_so_far <= max_ending_here):   #should this be lt or lteq?
            max_so_far = max_ending_here
            start_idx = start_idx_so_far
            stop_idx = i

    return start_idx_so_far, stop_idx, max_so_far
