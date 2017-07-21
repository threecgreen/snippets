from __future__ import print_function, division
import sys
from random import randint, seed
from enum import Enum
import numpy as np
range = xrange


def fix(over_under):
    """Create a skewed seed distribution."""
    seed_range = np.arange(1, 101)
    # Make each of the last 41 elements 5x more likely
    low = [1.0] * (len(seed_range) - 40)
    high = [5.0] * 40
    prob_dist = np.array(low + high if over_under == "over" else high + low)
    # Normalising to 1.0
    prob_dist = np.divide(prob_dist, np.sum(prob_dist))
    number = np.random.choice(seed_range, 1, p=prob_dist)
    return int(number)

def calc_pnl(style, bet, diff):
    """Calculate profit and loss for a given bet, bet style and difference between
    the line and the random number."""
    if style == "binary":
        return bet
    else:
        return bet * abs(diff)

def betting(times, bet, over_under, style):
    if over_under not in ("over", "under"):
        raise ValueError("Choose between betting over or under.")
    seed(fix(over_under))
    over = 6
    under = 5
    pnl = 0
    bet = float(bet)
    times = int(times)
    for time in range(times):
        num = randint(0, 11)
        if over_under == "over":
            if num > over:
                pnl += calc_pnl(style, bet, num - over)
            elif num == over:
                continue
            else:
                pnl -= calc_pnl(style, bet, num - over)
        else:
            if num < under:
                pnl += calc_pnl(style, bet, num - under)
            elif num == under:
                continue
            else:
                pnl -= calc_pnl(style, bet, num - under)

    if pnl > 0:
        print("You made {0:0.2f}".format(pnl))
    elif pnl < 0:
        print("You lost {0:0.2f}".format(abs(pnl)))


if __name__ == "__main__":
    betting(*sys.argv[1:])
