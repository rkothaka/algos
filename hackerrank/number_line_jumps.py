def kangaroo(x1, v1, x2, v2):
    # Write your code here
    def step_fn():
        nonlocal x1, x2
        x1 += v1
        x2 += v2

    # x1 - x2 increasing, decreasing, remains same
    # then abort
    pos_diff = x1 - x2
    while pos_diff != 0:
        sign = pos_diff > 0
        step_fn()
        new_pos_diff = x1 - x2
        new_sign = new_pos_diff > 0

        # fixed gap between two positions
        if new_pos_diff == pos_diff:
            return "NO"

        if sign == new_sign:
            # gap increasing
            if sign and new_pos_diff > pos_diff:
                return "NO"
            # gap increasing
            if not sign and new_pos_diff < pos_diff:
                return "NO"

        pos_diff = new_pos_diff

    return "YES"


if __name__ == "__main__":
    print(kangaroo(0, 3, 4, 2))
