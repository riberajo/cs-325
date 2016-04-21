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
        #def getResults(inputFile, algo, algoName, outputFile):
        #reads array/coins from input file and writes results to output file
        getResults(inputfile, changedp, "changedp", outputfile)
        print("Finished")
    else:
        print("Put filename in cmdline - python main.py [name].txt")

if __name__ == "__main__":
    main()
