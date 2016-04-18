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

def randomArrayGen():
    # Pushes random numbers into an array of size 100
    myRandomArr = []
    for i in range (100):
        myRandomArr.append(random.randrange(-100,100,1))
    return myRandomArr

def randomTest(algo1, algo2, algo3, algo4):
    myArr = randomArrayGen()
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

def getTimes(algo, n):
    myArr = randomArrayGen()
    runningTime = 0

    #start clock
    start = time.clock()
    for i in range(0, n):
        result1 = algo(myArr)
    #stop clock
    algPlusForTime = time.clock() - start

    #for loop time
    #start clock
    start = time.clock()
    for i in range(0, n):
        pass
    #stop clock
    forTime = time.clock() - start

    #find the difference
    runningTime = algPlusForTime - forTime

    #return average
    return runningTime
    
def getAlgTime(algo, algoName, n):
    algoTime = 0
    # Gets a  random generated array and calculates the time taken to execute  
    for i in range(0, 10):
        algoTime += getTimes(algo, n)

    algoTime /= 10
    print algoName, " time = ", algoTime, " seconds for n = ", n 

def plotTimes(algo, algoName, iterations):
    
    for n in iterations:
        getAlgTime(algo, algoName, n)

