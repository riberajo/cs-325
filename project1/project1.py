import os

# For enum calculations
def enum_msa(array):
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


def betterEnum_msa(array):
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
            
            
def main():
    myArr = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11];
    # test answer [8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19], 34
    enum_result = (enum_msa(myArr))
    print("enum", myArr[enum_result[0]:enum_result[1]+1])

    betterEnum_result = (better_msa(myArr))
    print("better enum", myArr[betterEnum_result[0]:betterEnum_result[1]+1])


if __name__ == "__main__":
    main()
