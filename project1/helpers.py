import random
import time

def getArrFromFile(src):
    arrData = []
    with open(src) as file:
        for line in file:
            #remove space and brackets
            line = line.replace('[', '').replace(' ', '').replace(']', '')
            #create list
            arrData.append([int(num) for num in line.split(',') if num not in '\n'])

    return arrData


def getResults(src, algo, algoName, myArr=[[]]):
    #get list of arrays
    if myArr == [[]]:
        myArr = getArrFromFile('MSS_Problems.txt')

    file = open(src, "a")
    file.write("\n"+algoName+"\n")

    #loop through list of arrays and write results to file
    for i in range(len(myArr)):
        testArray = myArr[i]
        result = algo(testArray)
        maxSum = result[2]
        subArr = testArray[result[0]:result[1]+1]
        writeData(file, testArray, subArr, maxSum)

def writeData(file, Arr, subArr, maxSum):
    # Writes original array, sub array, and max for each line in file
    file.write('{0}\n'.format(Arr))
    file.write('{0}\n'.format(subArr))
    file.write('{0}\n\n'.format(maxSum))

def randomArrayGen(n):
    # Pushes random numbers into an array of size n
    myRandomArr = []
    for i in range (n):
        myRandomArr.append(random.randrange(-100,100,1))
    return myRandomArr

def randomTest(algo1, algo2, algo3, algo4):
    myArr = randomArrayGen(100)
    src = "MSS_Error.txt"
    
    result1 = algo1(myArr)
    result2 = algo2(myArr)
    result3 = algo3(myArr)
    #DEBUGGING: print "**********************RUNNING RANDOM ALGORITHM 4***********************************"
    result4 = algo4(myArr)
    
    if result1 != result2:
        print "ERROR"
        print "Algorithm 1 and Algorithm 2 do not agree on the following array: ", myArr
    if result3 != result4:
        print "ERROR"
        print "Algorithm 3 and Algorithm 4 do not agree on the following array: ", myArr
        if result3 != result1:
            if result3 != result2:
                print "ERROR"
                print "Algorithm 3 is wrong on the following array: ", myArr
                print "See MSS_Error.txt"
                getResults(src, algo3, "ERROR: linearTime_msa", [myArr])
                getResults(src, algo1, "CORRECT ANSWER:", [myArr])
        if result4 != result1:
            if result4 != result2:
                print "ERROR"
                print "Algorithm 4 is wrong on the following array: ", myArr
                print "See MSS_Error.txt"
                getResults(src, algo4, "ERROR: linearTime_msa", [myArr])
                getResults(src, algo1, "CORRECT ANSWER:", [myArr])
    else:
        print("Test passed")

def getTimes(algo, algoName, n):
    myArr = randomArrayGen(n)

    #start clock
    start = time.time()
    for i in range(10):
        result1 = algo(myArr)
    #stop clock
    algPlusForTime = time.time() - start

    #for loop time
    #start clock
    start = time.time()
    for i in range(10):
        pass
    #stop clock
    forTime = time.time() - start

    #find the difference
    runningTime = algPlusForTime - forTime

    #average
    runningTime /= 10
    print algoName, " time = ", runningTime, " seconds for n = ", n 

    #return total
    return runningTime

def plotTimes(algo, algoName, iterations):
    file = open("MSS_Timing.txt", "a")

    file.write("\n"+algoName+"\n")
    for n in iterations:
        time = getTimes(algo, algoName, n)
        file.write('\n'+'n = '+str(n)+' time = '+str(time)+' seconds')
