#!/usr/bin/env python

from algorithms import *
from helpers import *
import sys



def main():

    #start if there's additional cmd line args
    if len(sys.argv) > 1:
        #get input file name
        inputfile = sys.argv[1]
        #set output file name
        outputfile = inputfile.split('.')[0] + "change.txt"


        ###################### Change Dynamic Programming ######################
        #def getResults(inputFile, algo, algoName, outputFile):
        #reads array/coins from input file and writes results to output file
        getResults(inputfile, changedp, "changedp", outputfile)

        #def getCSVResults(coinArr, A_list, algo, outputFile):
        # Problem 4
        coinArr =  [1, 5, 10, 25, 50]
        A_list = range(2010, 2200, 5)
        getCSVResults(coinArr, A_list, changedp, "changedp_prob4.csv")

        # Problem 5 a
        coinArr =  [1, 2, 6, 12, 24, 48, 60]
        A_list = range(2000, 2200)
        getCSVResults(coinArr, A_list, changedp, "changedp_prob5a.csv")

        # Problem 5 b
        coinArr =  [1, 6, 13, 37, 150]
        A_list = range(2000, 2200)
        getCSVResults(coinArr, A_list, changedp, "changedp_prob5b.csv")

        # Problem 6
        coinArr =  [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        A_list = range(2000, 2200)
        getCSVResults(coinArr, A_list, changedp, "changedp_prob6.csv")

        print("Finished")
    else:
        print("Put filename in cmdline - python main.py [name].txt")

if __name__ == "__main__":
    main()
