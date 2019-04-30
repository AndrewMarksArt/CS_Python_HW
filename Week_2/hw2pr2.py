# Filename: hw2pr2.py
# Name: Andrew Marks
# Problem description: Sleepwalking student

import random
import time


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])


def rwpos(start, nsteps):
    """
    takes a start position and a number of steps and uses rs() to take a random step until all number of steps are taken
    :param start: int, starting position
    :param nsteps: int, number of random steps to take
    :return: int, end position after all number of random steps taken
    """
    if nsteps == 0:
        return
    else:
        print('Start is: ' + str(start))
        return rwpos(start + rs(), nsteps - 1)


def rwsteps(start, low, high):
    """
    Takes a start position for the sleep walking student and a low and high end point. The student will take random
    steps until the they reach one of the end points. It then returns a count of the total steps taken.
    :param start: int, typically in the middle of the low and high
    :param low: int
    :param high: int
    :return: int, count of steps taken until the student reaches an endpoint
    """
    location = '|' + '_' * (start - low) + '(ಠ_ಠ)' + '_' * (high - start) + '|'
    time.sleep(0.25)

    if start == low or start == high:
        print(location)
        return 1
    else:
        print(location,'\n')
        return 1 + rwsteps(start + rs(), low, high)

print(rwsteps(10, 0, 20))


def rwposPlain(start, nsteps):
    """
    Similar to rwpos, given a starting point and the number of steps this will return the endpoint after the number
    of random steps
    :param start: int, where to start
    :param nsteps: int, number of random steps to take
    :return: int, location after all random steps are taken
    """
    if nsteps == 0:
        return start
    else:
        return rwposPlain(start + rs(), nsteps - 1)


print(rwsteps(10, 0, 20))


def ave_signed_displacement(numtrials):
    """
    takes an int as the number of times the random walker will take 100 steps starting at 0, taking a list of those
    distances and then RETURNS the average distance traveled
    :param numtirals: number of time to run random walker (reposPlain) as an int
    :return: avg distance traveled after 100 steps from 0 as an int
    """
    distances = [rwposPlain(0, 100) for x in range(numtrials)]
    avg_distance = sum(distances) / len(distances)
    return avg_distance



def ave_squaredDisplacement(numtrials):
    """
    takes the distance the random walker traveled from 0 after 100 steps, squares the distances from the number of trials
    and returns the average squared distance
    :param numtrials: number of time to run random walker (reposPlain) as an int
    :return: avg squared distance traveled after 100 steps from 0 as an int
    """
    distances = [rwposPlain(0, 100) for x in range(numtrials)]
    sqr_distances = [n**2 for n in distances]
    avg_sqr_distances = sum(sqr_distances)/len(sqr_distances)
    return avg_sqr_distances


avg = ave_signed_displacement(10)
print('The average steps taken from start after 10 trials is  ', avg)

sqr = ave_squaredDisplacement(100000)
print('The average squared distance from start after 100000 trials is ', sqr)

"""
     To compute the average signed displacement for
     a random walker after 100 random steps, I created a list
     called distances that held the end positions of the walker
     after using rwposPlain starting at 0 and taking 100 steps.
     Once I had the distances I summed them and then divided 
     the sum by the length of the list to get the average.
     
     copied below is the results of the average distance from 
     0 (the starting position) after 10, 1000, 10000 trials 
     
     The average steps taken from start after 10 trials is   2.6
     The average steps taken from start after 1000 trials is   -0.164
     The average steps taken from start after 10000 trials is   0.031
     
     as we can see from the results the more times we run it the closer 
     to zero we get. since we start at 0 and each step has a 50/50 chance 
     we would expect a normal distribution centered around 0 since we are 
     summing the ending positions the negative and positive values can basically
     cancel each other our. With less runs such as the example above with 10
     there is a higher chance that one side (pos/neg) has more observation 
     leading to a number farther from 0.
     
     
     below is the copied out put from the average squared distances from 10, 100, 1000,
     10000, 100000 runs of 100 steps starting at zero and then 3 runs of 100000 with 
     N steps of 33, 222, and 42.
     
     The average squared distance from start after 10 trials of 100 steps is  207.2
     The average squared distance from start after 100 trials of 100 steps is  100.44
     The average squared distance from start after 1000 trials of 100 steps is 93.868
     The average squared distance from start after 10000 trials of 100 steps is 100.8348
     The average squared distance from start after 100000 trials of 100 steps is 99.30708
     
     The average squared distance from start after 100000 trials of 33 steps is 33.01112
     The average squared distance from start after 100000 trials of 222 steps is 221.42904
     The average squared distance from start after 100000 trials of 42 steps is 41.94696
     
     by squaring the distances we dont have to worry about negative runs cancelling out 
     positive runs and can capture the total distance traveled regardless of whether it was
     positive or negative. Again the shorter the number of trials the larger the variance 
     and we can see that the average is very close to the number of steps being taken which 
     makes sense since we are looking at the average distance traveled away from the start.
"""

