from typing import List


def evaluate(expression: str) -> int:
    intermediate_results: List[int] = []
    delimiter = ','
    operators = {
        '+': lambda x, y: x + y, '-': lambda x, y: x - y,
        '*': lambda x, y: x * y, '/': lambda x, y: x / y,
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
        return intermediate_results[-1]
