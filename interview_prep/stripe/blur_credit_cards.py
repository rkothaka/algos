import re
from typing import List


def blur_credit_card(card: str) -> str:
    last_four_digits = card[-4:]
    blurred_part = re.sub(r'\d', 'X', card[:-4])
    return blurred_part + last_four_digits


def blur_credit_cards(cards: List[str]) -> List[str]:
    return [blur_credit_card(card) for card in cards]


if __name__ == '__main__':
    # Example usage:
    credit_cards = ["1234-5678-9876-5432", "9876-5432-1234-5678", "1111-2222-3333-4444"]
    blurred_cards = blur_credit_cards(credit_cards)

    for card in blurred_cards:
        print(card)
