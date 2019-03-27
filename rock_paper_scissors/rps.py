#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcomes = []
    choices = ["rock", "paper", "scissors"]  # possible choices

    # inner recursive function to add outcomes
    def get_outcome(rounds_left, result=[]):
        # base case: no rounds remain
        if rounds_left == 0:
            outcomes.append(result)
            return
        for choice in choices:
            get_outcome(rounds_left - 1, result + [choice])

    get_outcome(n)
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
