#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = None
    for key, val in recipe.items():
        if key not in ingredients.keys():
            return 0
        can_make = ingredients[key] // val
        if max_batches is None or can_make < max_batches:
            max_batches = can_make

    return max_batches


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )
