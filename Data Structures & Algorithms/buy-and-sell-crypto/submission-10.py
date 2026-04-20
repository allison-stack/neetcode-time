class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is buy, right is sell
        l, r = 0, 1
        m = 0
        while r < len(prices):
            # check if profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                m = max(m, profit)
            # found low price so shift left pointer there
            else:
                l = r
            # increment right pointer either way
            r += 1
        return m