from interview_prep.meta.puzzles.max_expected_profit import get_max_expected_profit, get_max_expected_profit_dp


def test_get_max_expected_profit1():
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 0.0
    expected_return_value = 25.0
    assert get_max_expected_profit(N, V, C, S) == expected_return_value


def test_get_max_expected_profit2():
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 1.0
    expected_return_value = 9.0
    assert get_max_expected_profit(N, V, C, S) == expected_return_value


def test_get_max_expected_profit3():
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.5
    expected_return_value = 17.0
    assert get_max_expected_profit(N, V, C, S) == expected_return_value


def test_get_max_expected_profit4():
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.15
    expected_return_value = 20.10825
    assert get_max_expected_profit(N, V, C, S) == expected_return_value


def test_get_max_expected_profit_dp():
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.15
    expected_return_value = 20.10825
    assert abs(get_max_expected_profit_dp(N, V, C, S) - expected_return_value) < 0.00001
