from typing import List
from functools import lru_cache


def get_max_expected_profit(N: int, V: List[int], C: int, S: float) -> float:
    profits = [0.0] * N

    balance_amount = 0.0
    for day in range(N - 1):
        enter_mail_room = balance_amount + V[day] - C
        balance_amount = (balance_amount + V[day]) * (1 - S)

        prev_day = 0.0 if N == 0 else profits[day - 1]
        if enter_mail_room >= balance_amount:
            profits[day] = prev_day + enter_mail_room
            balance_amount = 0.0
        else:
            profits[day] = prev_day

    last_day_expected = balance_amount + V[N - 1]
    if N > 1:
        profits[-1] = profits[-2]
    profits[-1] += max(last_day_expected - C, 0.0)

    return profits[-1]


def get_max_expected_profit_dp(N: int, V: List[int], C: int, S: float) -> float:
    @lru_cache(None)
    def helper(day: int, value_in_mail_room: float):
        if day >= N:
            return 0

        score = 0
        if value_in_mail_room + V[day] > C:
            score = value_in_mail_room + V[day] - C + helper(day + 1, 0)
        score = max(score, helper(day + 1, (value_in_mail_room + V[day]) * (1 - S)))

        return score

    return helper(0, 0.0)
