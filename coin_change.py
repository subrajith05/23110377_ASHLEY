import math
def ccp(n, target, coins):
    coins.sort()
    if target < coins[-1]:
        return -1
    
    dp = [[None for i in range(target+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for j in range(1, target+1):
        dp[0][j] = j//coins[0] if j%coins[0] == 0 else math.inf
    for i in range(1, n):
        for j in range(1, target+1):
            take = math.inf
            if j - coins[i] >= 0:
                take = 1 + dp[i][j-coins[i]]
            dp[i][j] = min(dp[i-1][j], take)
    return -1 if dp[-1][-1] == math.inf else dp[-1][-1]


n, target = (int(num) for num in input("Enter n and target: ").split())
coins = [int(num) for num in input("Enter coin values separated by space: ").split()]
print("Min no. of coins require:",ccp(n, target, coins))

#Sample input
# 3 11
# 1 5 6
