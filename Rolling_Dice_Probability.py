"""
In this program we can simulate the rolling of dice based on the input received from the user about the sides of the dice
and number of dice used and calculate the probability of each out come and tabulate it
"""

from random import randint
from collections import Counter

def Roll_Dice(*dice):
    num_trials = 10000
    counts = Counter()
    for roll in range(num_trials):
        """Setting up counts to count the randint for min of 1 and sides defined in the variable dice"""
        counts[sum((randint(1,sides) for sides in dice))] += 1

    print('\n Outcome \t Probability')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))# printing outcome and probability in the required format


if __name__ == '__main__':
    Roll_Dice(6,6)

