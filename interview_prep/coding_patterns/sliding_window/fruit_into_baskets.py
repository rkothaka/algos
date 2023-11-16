"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""


def totalFruit(self, fruits: List[int]) -> int:
    left = right = 0

    max_fruits = 0
    recent = {}
    while right < len(fruits):
        if len(recent) == 2 and fruits[right] not in recent:
            old, old_pos = None, float('inf')
            for key, pos in recent.items():
                if pos < old_pos:
                    old, old_pos = key, pos

            left = old_pos + 1
            del recent[old]

        recent[fruits[right]] = right
        right += 1

        max_fruits = max(max_fruits, right - left)

    return max_fruits
