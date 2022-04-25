# This function is used in choice 1
def impliedOdds(amount_remaining, pot, call_amount):
    pot = call_amount + pot
    return (amount_remaining + pot) / call_amount


# This function is used in choice 2
def betCalc(a, b):
    b = a + b
    return a / b


# This function is used in choice 3
def find_M(stack, SB, BB, antes, players):
    antes = antes * players
    return stack / (SB + BB + antes)


# This function is used in choice 4
def howMuchToRaise(stackSize, lastBet, moneyInPot, facingA):
    if facingA in "1":
        if stackSize > 60:
            return 2.75 * lastBet + moneyInPot
        if 35 <= stackSize < 60:
            return 2.5 * lastBet + moneyInPot
        if 22 <= stackSize < 35:
            return 2.25 * lastBet + moneyInPot
        if 12 <= stackSize < 22:
            return 2 * lastBet + moneyInPot
        if stackSize < 12:
            return "Go All In"
    if facingA in "2":
        if stackSize > 60:
            return 4.5 * lastBet + moneyInPot
        if 35 <= stackSize < 60:
            return 4.25 * lastBet + moneyInPot
        if 22 <= stackSize < 35:
            return 4 * lastBet + moneyInPot
        if 12 <= stackSize < 22:
            return 3.5 * lastBet + moneyInPot
        if stackSize < 12:
            return "Go All In"
    if facingA == "3":
        if stackSize > 60:
            a = 3 * lastBet + moneyInPot
            b = 4 * lastBet + moneyInPot
            return [a, b]

        if 35 <= stackSize < 60:
            a = 2.7 * lastBet + moneyInPot
            b = 3.2 * lastBet + moneyInPot
            return [a, b]

        if 22 <= stackSize < 35:
            a = 2.7 * lastBet + moneyInPot
            b = 3.2 * lastBet + moneyInPot
            return [a, b]

        if 12 <= stackSize < 22:
            return "Go All In"
        if stackSize < 12:
            return "Go All In"

    if facingA == "4":
        if stackSize > 60:
            a = 2.75 * lastBet + moneyInPot
            b = 3.25 * lastBet + moneyInPot
            return [a, b]

        if 35 <= stackSize < 60:
            a = 2.5 * lastBet + moneyInPot
            b = 3 * lastBet + moneyInPot
            return [a, b]

        if 22 <= stackSize < 35:
            return "Go All In"

        if 12 <= stackSize < 22:
            return "Go All In"
        if stackSize < 12:
            return "Go All In"


# This function is used in choice 5
def EV(percentTimesIWin, moneyWillWin, moneyILose, percentILose):
    percentTimesIWin = percentTimesIWin / 100
    return (percentTimesIWin * moneyWillWin) + (percentILose * -moneyILose)

