#!/usr/bin/env python

from algorithms import *
from helpers import *
from changedp_problems import *
from changegreedy_problems import *

import sys



def main():

    #start if there's additional cmd line args
    if len(sys.argv) > 1:
        #get input file name
        inputfile = sys.argv[1]
        #set output file name
        outputfile = inputfile.split('.')[0] + "change.txt"
        getChangedpData(inputfile, outputfile)
        getChangeGreedyData(inputfile, outputfile)

        print("Running bruteforce alg, for sample data it took ~20+ minutes")
        getResults(inputfile, changeslow, "changeslow", outputfile)

        print("Finished")
    else:
        print("Put filename in cmdline - python main.py [name].txt")

if __name__ == "__main__":
    main()
