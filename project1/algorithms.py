from math import floor

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
def recursive_msa(left_bound=0, right_bound=0, array=[]):
    left_max, mid_max, right_max, sub_max, total_sum = [0,0,0,0,0]
    max_left_side, max_right_side = [-1000000, -1000000]
    
    #Check if the is only one variable left
    if (left_bound == right_bound):
        return right_bound, left_bound, array[left_bound]
    
    #Find the maximum subarrays on the left and right
    #DEBUGGING: print "Calling recursive_msa from ", left_bound+int(floor((right_bound-left_bound)/2))+1, " to ", right_bound, " for right max"
    start_idx_right, stop_idx_right, right_max = recursive_msa(left_bound+int(floor((right_bound-left_bound)/2))+1, right_bound, array)
    #DEBUGGING: print "Calling recursive_msa from ", left_bound, " to ", left_bound+int(floor((right_bound-left_bound)/2)), " for left max"
    start_idx_left, stop_idx_left, left_max = recursive_msa(left_bound, left_bound+int(floor((right_bound-left_bound)/2)), array)
    
    #Maximum for a middle sub array array
    #Find max on left side
    for i in range(left_bound+int(floor((right_bound-left_bound)/2)), left_bound-1, -1):
        total_sum += array[i]
        #Update the left side maximum
        if (total_sum > max_left_side):
            max_left_side = total_sum
            start_idx_mid = i
    total_sum = 0

    #Find max on right side
    for i in range(left_bound+int(floor((right_bound-left_bound)/2))+1,right_bound+1):
        total_sum += array[i]
        #Update the right side maximum
        if (total_sum > max_right_side):
            max_right_side = total_sum
            stop_idx_mid = i
    
    mid_max = max_left_side + max_right_side

    #Finds the biggest of the three and returns it
    if(left_max > right_max):
        sub_max = left_max
        start_idx, stop_idx = [start_idx_left, stop_idx_left]
    else:
        sub_max = right_max
        start_idx, stop_idx = [start_idx_right, stop_idx_right]
    if(mid_max > sub_max):
        sub_max = mid_max
        start_idx, stop_idx = [start_idx_mid, stop_idx_mid]

    return start_idx, stop_idx, sub_max

def recursive_msa_call(array=[]):
    start_idx, stop_idx, max = recursive_msa(0,len(array)-1, array)
    return start_idx, stop_idx, max


#Algorithm 4
def linearTime_msa(array=[]):
    max_so_far = array[0]
    max_ending_here = array[0]
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
            #DEBUGGING: print "New start_idx: ", start_idx_so_far
            start_idx = start_idx_so_far
            stop_idx = i
            #DEBUGGING: print "New stop_idx: ", i

    #DEBUGGING: print "RETURNING: start_idx = " 
    return start_idx, stop_idx, max_so_far
