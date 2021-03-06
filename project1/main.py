#!/usr/bin/env python

from algorithms import *
from helpers import *

def main():
   
    src = 'MSS_Results.txt'
    alg1name = 'Enumeration '
    alg2name = 'Better Enumeration '
    alg3name = 'Recursive'
    alg4name = 'Linear Time'

    #src, algo, algo name
    getResults(src, enum_msa, alg1name)
    getResults(src, betterEnum_msa, alg2name)
    getResults(src, recursive_msa_call, alg3name)
    getResults(src, linearTime_msa, alg4name)

    #uses randomly generated array and compares them to each other
    randomTest(enum_msa, betterEnum_msa, recursive_msa_call, linearTime_msa)

    #gets running times for various iteration numbers
    #Comment out what you don't need
    plotTimes(enum_msa, alg1name, [100, 200, 300, 400, 500, 550, 600, 650, 700, 750])
    plotTimes(betterEnum_msa, alg2name, [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
    plotTimes(recursive_msa_call, alg3name, [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    plotTimes(linearTime_msa, alg4name, [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    print("finished")
    
if __name__ == "__main__":
    main()
