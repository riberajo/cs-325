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


        #will be used to call functions, but for now just print file data
        arrData = getArrFromFile(inputfile)
        for i in arrData:
            coins = i[0]
            target = i[1]
            print(changedp(coins, target))
    else:
        print("Put filename in cmdline - python main.py [name].txt")

if __name__ == "__main__":
    main()
