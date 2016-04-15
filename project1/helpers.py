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
