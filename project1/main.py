from algorithms import *
from helpers import *

def main():
   
    src = 'MSS_Results.txt'
    alg1name = 'Enumeration '
    alg2name = 'Better Enumeration '

    #src, algo, algo name
    getResults(src, enum_msa, alg1name)
    getResults(src, enum_msa, alg2name)



if __name__ == "__main__":
    main()
