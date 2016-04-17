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
    plotAlltheTimes(enum_msa, betterEnum_msa, recursive_msa_call, linearTime_msa, alg1name, alg2name, alg3name, alg4name)
    print("finished")
    
if __name__ == "__main__":
    main()
