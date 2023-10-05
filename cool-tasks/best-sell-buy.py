def max_profit(prices):
        n = len(prices)
        if not prices or n < 2:
            return 0
        else:
            max_profit = 0
            min_price = prices[0]

            for i in range(1, n):
                if prices[i] < min_price:
                    min_price = prices[i]
                else:
                    c_profit = prices[i] - min_price
                    max_profit = max(max_profit, c_profit)
        return max_profit
