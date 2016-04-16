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


def getResults(src, algo, algoName):
    #get list of arrays
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
    myRandomArr = []
    for i in range (10):
        myRandomArr.append(random.randrange(-100,100,1))
    return myRandomArr

def randomTest(algo1, algo2):
    myArr = randomArrayGen()
    
    result1 = algo1(myArr)
    result2 = algo2(myArr)

    if result1 != result2:
        print("error")
    else:
        print("Test passed")

def getTimes(algo):
    myArr = randomArrayGen()

    #start clock
    start = time.clock()
    result1 = algo(myArr)
    #stop clock
    elapsedTime = time.clock() - start

    return elapsedTime

def getAlgTime(algo, algoName, numerations):

    for i in range(numerations):
        algoTime = getTimes(algo)

    print(algoName, algoTime, "iteration", i+1)

def plotAlltheTimes(algo1, algo2, algo1Name, algo2Name):
    iteration = 1000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))
    
    iteration = 10000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))
    
    iteration = 100000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))

    iteration = 1000000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))

    iteration = 10000000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))
    
    iteration = 100000000
    print(getAlgTime(algo1, algo1Name, iteration))
    print(getAlgTime(algo2, algo2Name, iteration))
    


    

        
        
        
