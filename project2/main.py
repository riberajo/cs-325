#!/usr/bin/env python

from algorithms import *
from helpers import *
import sys

def main():

    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        outputfile = inputfile.split('.')[0] + "change.txt"

        arrData = getArrFromFile(inputfile)
        for i in arrData:
            print(i[0], i[1])
    else:
        print("Put filename in cmdline - python main.py [name].txt")

if __name__ == "__main__":
    main()
