import random

#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

#Usage:

seed = 12001907

random.seed(12001907)

keyWord = keywordFromSeed(seed)

print(keyWord)   # Prints "MATH"
