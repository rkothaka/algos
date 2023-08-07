from typing import List


def num_combinations_for_final_score(final_score: int, individual_play_scores: List[int]) -> int:
    num_combinations = [[1] + [0] * final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = num_combinations[i - 1][j] if i >= 1 else 0
            with_this_play = num_combinations[i][j - individual_play_scores[i]] \
                if j >= individual_play_scores[i] else 0
            num_combinations[i][j] = with_this_play + without_this_play

    for row in num_combinations:
        print(row)

    return num_combinations[-1][-1]


if __name__ == '__main__':
    individual_play_scores = [2, 3, 7]
    print(num_combinations_for_final_score(12, individual_play_scores))

