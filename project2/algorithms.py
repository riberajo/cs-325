
#Algorithm 1



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
    minCoins = sortedCoins

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
    print minCoins
    print coinTotals

    return minCoins, coinTotals


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
