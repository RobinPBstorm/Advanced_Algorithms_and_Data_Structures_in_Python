# [1,2,5,10,20,50] 75

def make_change_bottom_up(coins: list[int], total: int):
    number_coin_by_total = [0] + [float('inf')] * total
    for n in range(1, total + 1):
        available_coins = (c for c in coins if c <= n)
        for c in available_coins:
            number_coin_by_total[n] = min(number_coin_by_total[n], 1 +number_coin_by_total[n-c])
    print(number_coin_by_total)
    return number_coin_by_total[total] if number_coin_by_total[total] != float('inf') else -1 


from functools import cache


def make_change_memoization(coins: list[int], total: int):
    @cache
    def recurse(remaining: int):
        if remaining == 0:
            return 0
        if remaining in coins:
            return 1
        p = []
        available_coins = (c for c in coins if c <= remaining)
        for coin in available_coins:
            prev = recurse(remaining - coin)
            if (prev != -1):
                p.append(1 + prev)
        print(remaining, p)
        return min(p) if p else -1

    for value in range(total + 1):
        recurse(value)
    return recurse(total)

print(make_change_bottom_up([1,2,3], 6))
print(make_change_memoization([1,2,3], 6))