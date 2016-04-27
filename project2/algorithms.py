
#Algorithm 1
#Brute force algorithm. Count is correct but C[i] is not
def changeslow(coins, total):

     total_Count = total
     coins_used = [0] * len(coins)

     #for i in range(0, len(coins)):    
     #    if(sum(usedCoins) == total):
     #         return usedCoins, total_Count

     #else:
     count = 0 
     #used = [] 
     for i in range(0, len(coins)):
          if(coins[i] <= total):    
               used, count = changeslow(coins, total-coins[i]) 
               count = count + 1 
               used[i] = used[i] + 1   
        
    
               if (count < total_Count):
    
                    total_Count = count
                    coins_used[i] = used[i]  
     return coins_used, total_Count
#divide and conquer algorithm. Base case returns correctly but divide and conquer portion does not.
#def changeslow(coins, total):
#
#     coinsUsed = [0] * len(coins)
#     minCoins = 0 
#     for i in range(len(coins)):
#          if coins[i] ==total:
#               coinsUsed[i] = 1 
#               minCoins += 1
#               return(coinsUsed, minCoins);
#
#          else:
#               #minCoins = float('inf')
#               soln1=[]
#               soln2=[]  
#               for i in range(1, total):
#                    soln1 = changeslow(coins, i)
#                    soln2 = changeslow(coins, total-i)
          #sum1 = sum(soln1)
          #sum2 = sum(soln2)
          #count = soln1 + soln2
#                    if sum(soln1)+sum(soln2) < minCoins:
 #       
#                              minCoins = sum(soln1[i]) + sum(soln2[i]) 
#                              coinsUsed = [soln1[i] + soln2[i] for i in xrange (len(coins))]
#
#
 #    return (coinsUsed, minCoins);

#Algorithm 2
def changegreedy(coins, total):
    #set array to inf
    #minCoins =  [float("inf") for j in range(total+1)]
    # first val is 0
    #minCoins[0] = 0
    sortedCoins = []

    #arrays for getting used coins
    usedCoins = [0]*len(coins)
    coins_used = [0] * (total + 1)

    #sorted coins = coins we can use
    for i in reversed(coins):
        sortedCoins.append(i)

    #coin totals needed
    coinTotals = [total]
    minCoins = map(int,sortedCoins)

    for index, i in enumerate(coinTotals):
        coin_total = 0
        coins_used = 0
        temp = i
        for idx, j in enumerate(sortedCoins):
            minCoins[idx] = 0
            while (temp - j >= 0):
                minCoins[idx] += 1
                coins_used += 1
                coin_total += 1
                temp -= j
            coinTotals[index] = coin_total

    minCoins.reverse()

    #return minCoins, coinTotals
    return coinTotals[-1], minCoins


#Algorithm 3
#target = 11
#coins = 1,5,6,8
    #build matrix target by coins
    # 0 1 2 3 4 5 6 7 8 9 10 11
    #   1 2 3 4 5 6 7 8 9 10 11
    # 5 1 2 3 4 1 2 3 4 5 2  3
    # 6 1 2 3 4 1 1 2 3 4 2  2
    # 8 1 2 3 4 1 1 2 1 2 2  2
def changedp(coins, total):
    #set array to inf
    minCoins =  [float("inf") for j in range(total+1)]
    # first val is 0
    minCoins[0] = 0

    #arrays for getting used coins
    usedCoins = [0]*len(coins)
    coins_used = [0] * (total + 1)

    for i in range(1, total+1):
        if i == 0:
            last_coin_used = 0
        else:
            last_coin_used = 1

        for j in coins:
            if j <= i and minCoins[i-j]+1 < minCoins[i] :
                minCoins[i]  = minCoins[i-j] + 1
                last_coin_used = j

        coins_used[i] = last_coin_used

    coin = total
    while coin > 0:
        usedCoins[coins.index(coins_used[coin])] += 1
        coin -= coins_used[coin]

    return minCoins[-1], usedCoins
