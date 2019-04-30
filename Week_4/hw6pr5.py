# hw6pr5.py - Intro to loops!
# Name: Andrew Marks

import random


def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1, n+1):    # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!


# Tests for looping factorial
assert fac(0) == 1
assert fac(5) == 120


def power(b, p):
    """
    takes two parameters a base and power and returns the base raised to the power using a for loop
    :param b: int, the base
    :param p: int, power
    :return: return b**p
    """
    for x in range(0, b+1):
        result = x**p
    return result


# tests for looping power
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))


def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result


# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42


def summedOdds(L):
    """
    takes a list of ints, finds the odd elements in the list and sum them together
    :param L: list of ints
    :return: int, sum of odd elements of the list L
    """
    result = 0
    for x in L:
        if x%2 != 0:
            result += x
    return result


# tests!
assert summedOdds([4, 5, 6]) == 5
assert summedOdds(range(3, 10)) == 24


def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses


def untilARepeat(high):
    """
    guesses a random number from 0 to 'high' and adds it to a list L until the same number has been guessed twice
    :param high: int, the high end of the range for random guess
    :return: int, the count of the number of guesses need to find a match
    """
    L = []
    guess = random.choice(range(0, high))
    numguesses = 1
    while guess not in L:
        L = L + [guess]
        guess = random.choice(range(0, high))
        numguesses += 1
    return numguesses


L = [untilARepeat(365) for i in range(10000)]
print(L)
print(min(L))
print(max(L))
print(sum(L)/len(L))
print(42 in L)
