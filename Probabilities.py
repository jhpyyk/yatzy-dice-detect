import constant
import numpy as np

class Probabilities():
    def calc_probabilities(self, dice, throws_left):
        dice_counts = self.count_dice(dice)
        prob_arr = np.array([])

        # Upper section
        for i in range(0,6):
            prob_arr = np.append(prob_arr, self.calc_upper(dice_counts, throws_left, i)[-1])
        of_a_kinds = self.calc_of_a_kind(dice_counts, throws_left)

        # Pair
        prob_arr = np.append(prob_arr, of_a_kinds[1] + of_a_kinds[2] + 
                                       of_a_kinds[3] + of_a_kinds[4])

        # Two Pairs
        prob_arr = np.append(prob_arr, self.calc_two_pairs(dice_counts, throws_left)[-1])

        # Three-of-a-kind
        prob_arr = np.append(prob_arr, of_a_kinds[2] + of_a_kinds[3] + of_a_kinds[4])

        # Four-of-a-kind
        prob_arr = np.append(prob_arr, of_a_kinds[3] + of_a_kinds[4])

        # Small Straight
        prob_arr = np.append(prob_arr, self.calc_small_straight(dice_counts, throws_left)[-1])

        # Large Straight
        prob_arr = np.append(prob_arr, self.calc_large_straight(dice_counts, throws_left)[-1])

        # Full House
        prob_arr = np.append(prob_arr, 0)

        # Chance
        prob_arr = np.append(prob_arr, 1)

        # Yatzy
        prob_arr = np.append(prob_arr, of_a_kinds[4])



        return prob_arr

    def count_dice(self, dice):
        dice_counts = np.array([])
        dice = np.sort(dice)
        for i in range(1, 7):
            count = np.count_nonzero(dice == i)
            dice_counts = np.append(dice_counts, count)
        return dice_counts

    def calc_upper(self, dice_counts, throws_left, num):
        if (throws_left == 3):
            return np.linalg.matrix_power(constant.UPPER_SECTION_TRANSITION, 2)@(constant.UPPER_SECTION_INITIAL)

        initial_state = np.zeros(3)
        count = dice_counts[num]
        if (count > 3):
            count = 3
        elif (count == 0):
            return constant.UPPER_SECTION_INITIAL

        initial_state[int(count - 1)] = 1
        return np.linalg.matrix_power(constant.UPPER_SECTION_TRANSITION, throws_left)@initial_state
        

    def calc_of_a_kind(self, dice_counts, throws_left):
        if (throws_left == 3):
            return np.linalg.matrix_power(constant.OF_A_KIND_TRANSITION, 2)@constant.OF_A_KIND_INITIAL

        initial_state = np.zeros(5)
        # Forms the initial state vector from dice counts
        # Example: two same dice -> [0,1,0,0,0]
        initial_state[int(np.amax(dice_counts, axis=None) - 1)] = 1
        return np.linalg.matrix_power(constant.OF_A_KIND_TRANSITION, throws_left)@initial_state

    
    def calc_small_straight(self, dice_counts, throws_left):
        if (throws_left == 3):
            return np.linalg.matrix_power(constant.STRAIGHTS_TRANSITION, 2)@constant.STRAIGHTS_INITIAL

        initial_state = np.zeros(5)
        
        in_straight = np.count_nonzero(dice_counts[:-1])
        initial_state[in_straight - 1] = 1

        return np.linalg.matrix_power(constant.STRAIGHTS_TRANSITION, throws_left)@initial_state
    

    def calc_large_straight(self, dice_counts, throws_left):
        if (throws_left == 3):
            return np.linalg.matrix_power(constant.STRAIGHTS_TRANSITION, 2)@constant.STRAIGHTS_INITIAL

        initial_state = np.zeros(5)
        
        in_straight = np.count_nonzero(dice_counts[1:])
        initial_state[in_straight - 1] = 1

        return np.linalg.matrix_power(constant.STRAIGHTS_TRANSITION, throws_left)@initial_state
    
    def calc_two_pairs(self, dice_counts, throws_left):
        if (throws_left == 3):
            return np.linalg.matrix_power(constant.TWO_PAIRS_TRANSITION, 2)@constant.TWO_PAIRS_INITIAL

        initial_state = np.zeros(3)

        pairs = 0
        for count in dice_counts:
            if (count >= 2):
                pairs += 1
        
        initial_state[pairs] = 1

        return np.linalg.matrix_power(constant.TWO_PAIRS_TRANSITION, throws_left)@initial_state
        