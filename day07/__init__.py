from operator import attrgetter
from hand import Hand


def sort_hands(hands: list[Hand]) -> list[Hand]:
    return sorted(hands, key=attrgetter("total_score"), reverse=True)


