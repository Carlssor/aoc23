from enum import IntEnum


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, cards: str, with_joker=False):
        self._card_to_score = {
            "T": 10,
            "J": 1 if with_joker else 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        self._card_to_score.update((str(val), val) for val in range(2, 10))
        self._with_joker = with_joker
        self._cards = cards
        self._hand_type = self._get_hand_type()
        self._cards_score = self._get_cards_score()
        self.total_score = (int(self._hand_type), self._cards_score)

    def _get_amount_of_each_card(self, cards: str) -> dict[str, int]:
        amount_of_each_card = {}
        for card in cards:
            amount_of_each_card[card] = amount_of_each_card.get(card, 0) + 1
        return amount_of_each_card

    def _get_hand_type(self) -> HandType:
        if self._with_joker:
            amount_of_each_card = self._get_amount_of_each_card(self._cards.replace("J", ""))
            most_common_card = "A"
            for card in amount_of_each_card:
                if amount_of_each_card[card] > amount_of_each_card.get(most_common_card, 0):
                    most_common_card = card
            cards = self._cards.replace("J", most_common_card)
        else:
            cards = self._cards
        cards_set = set(cards)
        amount_different_cards = len(cards_set)
        if amount_different_cards == 1:
            return HandType.FIVE_OF_A_KIND
        elif amount_different_cards == 2:
            if cards.count(cards[0]) in (1, 4):
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        elif amount_different_cards == 3:
            for card in cards_set:
                if cards.count(card) == 3:
                    return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIRS
        elif amount_different_cards == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def _get_cards_score(self):
        return [self._card_to_score[card] for card in self._cards]
