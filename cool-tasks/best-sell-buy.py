def max_profit(prices):
    l, r = 0, 1
    max_prof = 0
    while r < len(prices):
        prof = prices[r] - prices[l]
        if prices[l] > prices[r]:
            l = r
        else:
            max_prof = max(prof, max_prof)
        r += 1
    return max_prof
