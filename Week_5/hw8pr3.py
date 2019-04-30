# hw8pr3.py
# Andrew Marks

import random, math


def throwDart():
    """
    takes a random number from -1, 1 as an x and y coordinate to create a point that the thrown dart hits
    :return: True, if the dart hits the circle and False if a miss
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    r = 1
    if x**2 + y**2 <= r**2:
        return True
    else:
        return False


def forPi(n):
    """
    throws n darts using thrownDart() and prints how many hits, throws and approx pi.
    :param n: int, number of throws
    :return: int, approx measure of pi
    """
    hits = 0
    for i in range(1, n+1):
        hits += 1 if throwDart() else 0
        pi = (hits/i)*4
        print(str(hits) + ' hits out of ' + str(i) + ' throws so that pi is ' + str(pi))

    return pi


def whilePi(error):
    """
    takes a floating point number and throws darts until the approx of pi is with in the error of actual pi
    :param error: float
    :return: int, how many throws needed to get to an approx pi with in the error
    """
    throws = 0
    hits = 0
    while throws == 0 or abs((hits / throws) * 4 - math.pi) > error:
        hits += 1 if throwDart() else 0
        throws += 1
        pi = (hits/throws) * 4
        print(str(hits) + ' out of ' + str(throws) + ' throws so pi is ' + str(pi))

    return throws


whilePi(0.005)
