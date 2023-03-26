"""
Each trial generates an outcome, such as landing on heads or tails.
The trial is repeated over and over again in order to calculate the propability
that a given outcomes occurs.
"""

import random
from enum import StrEnum, IntEnum, auto

heads_tally = 0
tails_tally = 0

unfair_heads_tally = 0
unfair_tails_tally = 0


class CoinSide(StrEnum):
    TAILS = auto()
    HEADS = auto()


class DieNumber(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


def coin_flip() -> enumerate:
    if random.randint(0, 1) == 0:
        return CoinSide.HEADS
    else:
        return CoinSide.TAILS


def unfair_coin_flip(propability_of_tails: float) -> enumerate:
    if random.random() < propability_of_tails:
        return CoinSide.TAILS
    else:
        return CoinSide.HEADS


def roll():
    match random.randint(1, 6):
        case 1:
            return DieNumber.ONE
        case 2:
            return DieNumber.TWO
        case 3:
            return DieNumber.THREE
        case 4:
            return DieNumber.FOUR
        case 5:
            return DieNumber.FIVE
        case 6:
            return DieNumber.SIX


for trial in range(10_000):
    if coin_flip() == CoinSide.TAILS:
        heads_tally += 1
    else:
        tails_tally += 1

for trial in range(10_000):
    if unfair_coin_flip(.7) == CoinSide.HEADS:
        unfair_heads_tally += 1
    else:
        unfair_tails_tally += 1

ratio = heads_tally / tails_tally
unfair_ratio = unfair_heads_tally / unfair_tails_tally
print(f"The ratio of heads to tails is {ratio}", end="\n")
print(f"The unfair ration of heads to tails is {unfair_ratio}")
