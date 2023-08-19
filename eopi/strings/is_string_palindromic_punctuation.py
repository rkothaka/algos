def is_palindromic(s: str) -> bool:
    parsed_s = map(str.lower, filter(str.isalnum, s))
    reversed_parsed_s = map(str.lower, filter(str.isalnum, reversed(s)))

    return all(a == b for a, b in zip(parsed_s, reversed_parsed_s))


if __name__ == "__main__":
    print(is_palindromic("A man, a plan, a canal, Panama"))
