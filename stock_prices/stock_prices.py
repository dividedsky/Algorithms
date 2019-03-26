#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = None
    lowest = None
    for i in range(len(prices) - 1):
        # find the highest sum for i: (the largest num in the array after i) - i
        if (
            lowest is None or prices[i] < lowest
        ):  # no need to search if we've already calculated for a lower value
            lowest = prices[i]
            best = max(prices[i + 1 :]) - prices[i]
            # replace max_profit if best is higher
            if max_profit == None or best > max_profit:
                max_profit = best

    return max_profit


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )
