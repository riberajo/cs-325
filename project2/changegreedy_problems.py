from algorithms import *
from helpers import *

def getChangeGreedyData(inputfile, outputfile):
    ###################### Change Dynamic Programming ######################
    #def getResults(inputFile, algo, algoName, outputFile):
    #reads array/coins from input file and writes results to output file
    getResults(inputfile, changegreedy, "changegreedy", outputfile)

    #def getCSVResults(coinArr, A_list, algo, outputFile):
    # Problem 4
    coinArr =  [1, 5, 10, 25, 50]
    A_list = range(2010, 2225, 5)
    getCSVResults(coinArr, A_list, changegreedy, "changegreedy_prob4.csv")
    plotTimes(changegreedy, "changegreedy", A_list, coinArr, "changegreedy_prob4Spd.csv")

    # Problem 5 a
    coinArr =  [1, 2, 6, 12, 24, 48, 60]
    A_list = range(100000, 100100)
    getCSVResults(coinArr, A_list, changegreedy, "changegreedy_prob5a.csv")
    plotTimes(changegreedy, "changegreedy", A_list, coinArr, "changegreedy_prob5aSpd.csv")

    # Problem 5 b
    coinArr =  [1, 6, 13, 37, 150]
    A_list = range(100000, 100100)
    getCSVResults(coinArr, A_list, changegreedy, "changegreedy_prob5b.csv")
    plotTimes(changegreedy, "changegreedy", A_list, coinArr, "changegreedy_prob5bSpd.csv")

    # Problem 6
    coinArr =  [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    A_list = range(100000, 100100)
    getCSVResults(coinArr, A_list, changegreedy, "changegreedy_prob6.csv")
    #def plotTimes(algo, algoName, iterations, coinArr):
    plotTimes(changegreedy, "changegreedy", A_list, coinArr, "changegreedy_prob6Spd.csv")
