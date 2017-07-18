from __future__ import print_function
import sys
from random import randint, seed
range = xrange


def calc_pnl(style, bet, diff):
    if style == "binary":
        return bet
    else:
        return bet * abs(diff)

def betting(times, bet, over_under, style):
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
