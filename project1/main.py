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
    plotTimes(enum_msa, alg1name, [50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
    plotTimes(betterEnum_msa, alg2name, [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
    plotTimes(recursive_msa_call, alg3name, [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    plotTimes(linearTime_msa, alg4name, [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    print("finished")
    
if __name__ == "__main__":
    main()
