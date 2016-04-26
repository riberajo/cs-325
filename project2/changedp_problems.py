from algorithms import *
from helpers import *

def getChangedpData(inputfile, outputfile):

    ###################### Change Dynamic Programming ######################
    #def getResults(inputFile, algo, algoName, outputFile):
    #reads array/coins from input file and writes results to output file
    getResults(inputfile, changedp, "changedp", outputfile)

    #def getCSVResults(coinArr, A_list, algo, outputFile):
    # Problem 4
    coinArr =  [1, 5, 10, 25, 50]
    A_list = range(2010, 2225, 5)
    getCSVResults(coinArr, A_list, changedp, "changedp_prob4.csv")
    plotTimes(changedp, "changedp", A_list, coinArr, "changedp_prob4Spd.csv")

    # Problem 5 a
    coinArr =  [1, 2, 6, 12, 24, 48, 60]
    A_list = range(2000, 2201)
    getCSVResults(coinArr, A_list, changedp, "changedp_prob5a.csv")
    plotTimes(changedp, "changedp", A_list, coinArr, "changedp_prob5aSpd.csv")

    # Problem 5 b
    coinArr =  [1, 6, 13, 37, 150]
    A_list = range(2000, 2201)
    getCSVResults(coinArr, A_list, changedp, "changedp_prob5b.csv")
    plotTimes(changedp, "changedp", A_list, coinArr, "changedp_prob5bSpd.csv")

    # Problem 6
    coinArr =  [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    A_list = range(2000, 2201)
    getCSVResults(coinArr, A_list, changedp, "changedp_prob6.csv")
    #def plotTimes(algo, algoName, iterations, coinArr):
    plotTimes(changedp, "changedp", A_list, coinArr, "changedp_prob6Spd.csv")
