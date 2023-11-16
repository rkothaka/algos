import random


# return random city with probability proportional to pop
def random_city(population: dict[str, int]) -> str:
    cities, pop_sum = [], []

    for city, pop in population.items():
        cities.append(city)
        prev_sum = pop_sum[-1] if pop_sum else 0
        pop_sum.append(prev_sum + pop)

    rand = random.randint(1, pop_sum[-1])
    return cities[bsearch(pop_sum, rand)]


def bsearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    population = {'NY': 7, 'SF': 5, 'Seattle': 8, 'Austin': 3}
    print(random_city(population))
