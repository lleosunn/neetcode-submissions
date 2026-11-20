class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # create an array of len(prices) where prices[n] contains the index
        # with the cheapest stock price before prices[n]
        # this takes O(n)
        # then iterate through prices again and compare it to the array

        cheapest_so_far = prices[0]
        cheap = []
        for p in prices:
            cheap.append(cheapest_so_far)
            cheapest_so_far = min(cheapest_so_far, p)
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - cheap[i])
        
        return max_profit

