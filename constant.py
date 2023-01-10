# Transition matrices for calculating the probabilities with a Markov Chain
# Calculated by hand
# A very helpful article about the subject is at:
# https://issuu.com/milliemince/docs/using_markov_chains_and_probabilistic_modeling_to_

import numpy as np

UPPER_SECTION_INITIAL = np.array([3125/7776, 1250/7776, 276/7776])

UPPER_SECTION_TRANSITION = np.array([[625/1296, 0, 0],
                                     [500/1296, 125/216, 0],
                                     [171/1296, 91/216, 1]])

OF_A_KIND_INITIAL = np.array([720/7776, 5400/7776, 1500/7776, 150/7776, 6/7776])

OF_A_KIND_TRANSITION = np.array([[120/1296, 0, 0, 0, 0],
                                 [900/1296, 120/216, 0, 0, 0],
                                 [250/1296, 80/216, 25/36, 0, 0],
                                 [25/1296, 15/216, 10/36, 5/6, 0],
                                 [1/1296, 1/216, 1/36, 1/6, 1]])

STRAIGHTS_INITIAL = np.array([156/7776, 1800/7776, 3900/7776, 1800/7776, 120/7776])

STRAIGHTS_TRANSITION = np.array([[16/1296, 0, 0, 0, 0],
                                 [260/1296, 27/216, 0, 0, 0],
                                 [660/1296, 111/216, 16/36, 0, 0],
                                 [336/1296, 72/216, 18/36, 5/6, 0],
                                 [24/1296, 6/216, 2/36, 1/6, 1]])

TWO_PAIRS_INITIAL = np.array([720/7776, 4956/7776, 2100/7776])

TWO_PAIRS_TRANSITION = np.array([[720/7776, 0, 0],
                                 [4956/7776, 152/216, 0],
                                 [2100/7776, 64/216, 1]])

FULL_HOUSE_INITIAL = np.array([])

FULL_HOUSE_TRANSITION = np.array([])