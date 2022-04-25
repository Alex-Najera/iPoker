from functions import *


def main():
    n = 1
    print("Welcome to iPoker")
    print(n, "======================================================")
    n += 1
    while True:
        choice = int(
            input("Please enter the number of the tool you want to use \n"
                  "\n[+]1. Implied Odds Calculator \n"
                  "\n[+]2. Bet needs to work calculator \n"
                  "\n[+]3. Find M \n"
                  "\n[+]4. How much to raise \n"
                  "\n[+]5. EV Calc \n"
                  ))

        if choice == 1:
            print(n, "======================================================")
            n += 1
            while True:
                try:
                    amountRemaining = float(input("Please enter the amount remaining in the effective stack(0 to exit> "))
                    if amountRemaining == 0:
                        break
                    pot = float(input("Please enter the pot(0 to quit)> "))
                    if pot == 0:
                        break
                    callAmount = float(input("Please enter the call amount(0 to quit)> "))
                    if callAmount == 0:
                        break
                    print(n, "======================================================")
                    n += 1
                    x = round(impliedOdds(amountRemaining, pot, callAmount), 1)
                    print(f"The implied odds are {x} : 1")

                    if x >= 9.5:
                        print("You can continue with small pairs")
                    if x >= 19.5:
                        print("You can continue with suited connectors.")
                        print("You can continue with suited Aces.")
                except ValueError:
                    print("Enter a number.")
                    continue
                print(n, "======================================================")
                n += 1
                break

        if choice == 2:
            print(n, "======================================================")
            n += 1
            while True:
                try:
                    betAmount = float(input("Please enter the amount of your bet(0 to quit)> "))
                    if betAmount == 0:
                        break
                    potAfterBet = float(input("Please enter the pot amount(0 to quit)> "))
                    if potAfterBet == 0:
                        break
                    result = str(betCalc(betAmount, potAfterBet))
                    print()
                    print(f"This bet needs to word {result[2:4]}% of the time.")
                    print(f"Your opponent needs to defend with {100 - int(result[2:4])}% of his range.")
                    print()
                except ValueError:
                    continue
                print(n, "======================================================")
                n += 1
                break
        if choice == 3:
            print(n, "======================================================")
            n += 1
            while True:
                try:
                    stack_size = int(input("Enter your stack size in chips(not BB's)(0 to exit)> "))
                    if stack_size == 0:
                        break
                    SB = int(input("Enter the Small Blind> "))
                    BB = int(input("Enter the Big Blind> "))
                    Ante = int(input("Enter the Ante> "))
                    players = int(input("Enter the amount of players at the table> "))
                    # x = round(find_M(stack_size,SB, BB, Ante, players), 1)
                    x = int(find_M(stack_size, SB, BB, Ante, players))
                    print()
                    print(f"Your M is {x}")
                    print()
                    if x > 20:
                        print("The Green Zone\n"
                              "We have enough time to be patient and wait for strong holdings,\n"
                              "but we also have the freedom to dabble with more speculative hands and play aggressively.")
                        print()
                    if 10 <= x <= 20:
                        print("The Yellow Zone\n"
                              "Now we are starting to feel the time pressure a little bit. We must start looking\n"
                              "for spots to get involved and play hands.")
                        print()
                    if 6 <= x < 10:
                        print("The Orange Zone\n"
                              "The pressure tightens here, and we want to avoid wasting any chips. Cold-calling starts\n"
                              "to become risky. Our main focus should be trying to be the first player involved in the pot,\n "
                              "wherever possible.")
                        print()
                    if 1 <= x < 6:
                        print()
                        print("The Red Zone\n"
                              "Move all-in or fold.")
                        print()
                    print(n, "======================================================")
                    n += 1

                except ValueError:
                    print("Enter a number.")
                    continue
                except ZeroDivisionError:
                    print("Cannot be Zero")
                    continue
                break
        if choice == 4:
            print(n, "======================================================")
            n += 1
            while True:
                try:
                    stack_size = float(input("Enter your stack size(Enter 0 to Exit)> "))
                    if stack_size == 0:
                        break
                    lastBet = float((input("Enter the last bet> ")))
                    moneyInPot = float((input("Enter the money in the pot> ")))
                    facingA = str(input("Did he 1.fold, 2.limp, 3.raise, or 4.3-bet?> "))
                    percentage = stack_size * 0.3
                    if facingA == "3":
                        print()
                        print(
                            f"You should raise {round(howMuchToRaise(stack_size, lastBet, moneyInPot, facingA)[0], 1)} BB's in "
                            f"position or {round(howMuchToRaise(stack_size, lastBet, moneyInPot, facingA)[1], 1)} out of "
                            f"position.")
                        print()
                        print(n, "======================================================")
                        n += 1
                    else:
                        print()
                        print(f"You should raise {howMuchToRaise(stack_size, lastBet, moneyInPot, facingA)} BB's or chips.")
                        print()
                        print(n, "======================================================")
                        n += 1
                except ZeroDivisionError:
                    print("Cannot be Zero")
                    continue
                except ValueError:
                    print("Enter correct key")
                    continue
                break
        if choice == 5:
            print(n, "======================================================")
            n += 1
            while True:
                try:
                    percentTimesIWin = float(input("Percent times you win(0 to exit)> "))
                    if percentTimesIWin == 0:
                        break
                    moneyIWin = float(input("Money I win> "))
                    moneyILose = float(input("Money I lose> "))
                    percentILose = float(input("Enter the percent of times you lose.> "))
                    print()
                    print(f"Your EV is> {EV(percentTimesIWin, moneyIWin, moneyILose, percentILose)}")
                    print(n, "======================================================")
                    n += 1
                except ValueError:
                    print("Enter correct key")
                    continue
                break


if __name__ == '__main__':
    main()
