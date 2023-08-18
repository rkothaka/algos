import collections
from typing import List


def change(money: int, coin_denominations: List[int], d: int) -> List[int]:
    CoinsSelected = collections.namedtuple('CoinsSelected', ('total_count', 'individual_counts'))

    # Setup base case
    min_coins = [CoinsSelected(float('inf'), [0] * d) for _ in range(money + 1)]
    min_coins[0] = CoinsSelected(0, [0] * d)

    for coin_idx in range(d):
        for amount in range(coin_denominations[coin_idx], money + 1):
            current_individual_counts = min_coins[amount - coin_denominations[coin_idx]].individual_counts.copy()
            current_individual_counts[coin_idx] += 1

            current_total_count = min_coins[amount - coin_denominations[coin_idx]].total_count + 1

            if min_coins[amount].total_count > current_total_count:
                min_coins[amount] = CoinsSelected(current_total_count, current_individual_counts)

    return min_coins[money].individual_counts if min_coins[money].total_count != float('inf') else None


if __name__ == '__main__':
    coin_denominations = [1, 5, 10, 20, 25]
    d = len(coin_denominations)
    money = 77

    counts = change(money, coin_denominations, d)
    for i in range(d):
        print(f'{counts[i]} of {coin_denominations[i]}')
