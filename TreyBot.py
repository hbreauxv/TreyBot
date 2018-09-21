#! /usr/bin/env python3

# TreyBot.py is an AI that tries to guess your number.  
# He'll start by guessing zero, and then randomly choose to either: Add 1, Subtract 1, Multiply by 2, or Divide by 2. 
# If the new guess is closer to your target number, TreyBot will be more likely to choose the operation that brought him closer in the future.  

# TreyBot has 100 guesses.  If he can't get your number in that many, he loses.  The bigger the number, the harder it is for TreyBot to guess. \

import logging, random

# Logging configuration
logging.basicConfig(filename='ai_reach_50_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Starting Program...')


# Initialize a random number.  May change this to a random number between 1-100 in the future actually.

n = int(input('TreyBot: Welcome. I am an AI that guesses random numbers.  Input a number please:'))
logging.info('n = {}'.format(n))
print('TreyBot: My target Number is {}.  Let the guessing begin!'.format(n))


class Operations:

    # Score attribute is unused right now
    score = 1


class Add(Operations):

    def math(self):
        global n
        n = n + 1
        return n


class Subtract(Operations):

    def math(self):
        global n
        n = n - 1
        return n


class Multiply(Operations):

    def math(self):
        global n
        n = n * 2
        return n


class Divide(Operations):

    def math(self):
        global n
        n = n / 2
        return n


def TreyBot():
    # Create list of functions
    global n
    # Set our target because we coded poorly and dont want to change all of our old n's to something else
    target = n
    # Start us at 0 boss
    n = 0
    mathlist = [Add, Subtract, Multiply, Divide]
    for i in range(100):
        compare = n

        # Pick a random function from the list and use it
        m = random.choice(mathlist)
        m.math(n)
        logging.info('Picked {}, n = {}'.format(m, compare))

        # Check which number is closest to 50
        closer = min([compare,n], key=lambda x: abs(x-target))
        # Uncomment these if you want to watch the program try different numbers
        # print("n is {}".format(n))
        # print("compare is {}".format(compare))
        # print("closer is {}".format(closer))

        # If it makes use closer to 50 than before, give that function a point/ add it to the list
        if n == closer:
            mathlist.append(m)
            m.score = m.score + 1
        n = int(closer)

        # Check if we hit 50
        if n == target:
            return "TreyBot: I did it! n = {}!!! Achieved in {} tries".format(target, i)
    return "TreyBot: I failed! {} tries reached. " \
           "My number is {} and I didnt get to target number {}".format(i, n, target)


print(TreyBot())
