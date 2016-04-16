from algorithms import *
from helpers import *

def main():
   
    src = 'MSS_Results.txt'
    alg1name = 'Enumeration '
    alg2name = 'Better Enumeration '

    #src, algo, algo name
    getResults(src, enum_msa, alg1name)
    getResults(src, betterEnum_msa, alg2name)

    #uses randomly generated array and compares them to each other
    randomTest(enum_msa, betterEnum_msa)

    #gets running times for various iteration numbers
    plotAlltheTimes(enum_msa, betterEnum_msa, alg1name, alg2name)
    
if __name__ == "__main__":
    main()
