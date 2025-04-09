# 121. Best Time to Buy and Sell Stock

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    profitMax = 0
    currLowest = prices[0]
    for i in range(len(prices)):
        if(currLowest >= prices[i]):
            currLowest = prices[i]
        profit = prices[i] - currLowest
        profitMax = max(profitMax, profit)
    return profitMax