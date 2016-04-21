import random
import time
import numpy as np

def getArrFromFile(src):
    arrData = []
    with open(src) as file:
        while True:
            line1 = file.readline().strip().strip(']').strip('[').replace(' ','').split(',')
            line2 = file.readline().strip()
            line1Arr = [int(x) for x in line1 if x != '']
            if not line2:
                break
            arrData.append([line1Arr, int(line2)])

    return arrData


def getResults(inputFile, algo, algoName, outputFile):
    #get list of arrays
    myArr = getArrFromFile(inputFile)

    file = open(outputFile, "a+")
    file.write("\n"+ "Algorithm:"+algoName+"\n")

    #loop through list of arrays and write results to file
    for i in myArr:
        coins = i[0]
        target = i[1]
        result = algo(coins, target)
        coinArr = result[1]
        coinsUsed = result[0]
        writeData(file, coinArr, coinsUsed)
    file.close()

def writeData(file, Arr, coinsUsed):
    file.write('{0}\n'.format(Arr))
    file.write('{0}\n'.format(coinsUsed))

def getCSVResults(coinArr, A_list, algo, outputFile):
    datafile_id = open(outputFile, 'a+')

    myArr = []
    for i in A_list:
        results = algo(coinArr, i)
        myArr.append(results[0])

    yarray = np.array(myArr)
    xarray = np.array(A_list)

    data = np.array([xarray, yarray])
    data = data.T

    np.savetxt(datafile_id, data, fmt=['%d','%d'])

    datafile_id.close()


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

def getTimes(algo, algoName, n, coinArr):

    #start clock
    start = time.time()
    for i in range(10):
        result1 = algo(coinArr, n)
    #stop clock
    runningTime = time.time() - start

    #average
    runningTime /= 10
    #print algoName, " time = ", runningTime, " seconds for n = ", n

    #return total
    return runningTime

def plotTimes(algo, algoName, iterations, coinArr, outputFile):
    file = open(outputFile, "a+")
    timeArr = []
    np.set_printoptions(precision=6)
    for n in iterations:
        time = getTimes(algo, algoName, n, coinArr)
        timeArr.append(time)
        if n % 13 == 0:
            print("working")

    yarray = np.array(timeArr)
    xarray = np.array(iterations)

    data = np.array([xarray, yarray])
    data = data.T

    np.savetxt(file, data, fmt=['%d','%.6f'])

    file.close()
