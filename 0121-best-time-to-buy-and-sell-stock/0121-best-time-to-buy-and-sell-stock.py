class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minn=prices[0]

        for i in range(1,len(prices)):
            if prices[i]-minn > profit:
                profit = prices[i]-minn
            minn=min(minn,prices[i])

        return profit

