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
