# 322. Coin Change

def coinChange(self, coins: List[int], amount: int) -> int:

    res = -1
    dp = [0] * (amount + 1)

    for i in range(1, amount + 1):
        tmp = float('inf')
        for coin in coins:
            if i-coin >= 0:
                tmp = min(tmp, dp[i-coin] + 1)
        dp[i] = tmp
    
    return dp[amount] if dp[amount] != float('inf') else -1