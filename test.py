from itertools import product
from itertools import combinations
from itertools import permutations

list1 = list(product(range(1,7), repeat=5))

def initial_4():
    possible = 0
    for throw in list1:
        pairs = 0
        for i in range(1,7):
            if(throw.count(i) >= 2):
                pairs += 1
        if (pairs == 2):
            possible += 1

    return possible

def initial_2():
    possible = 0
    for throw in list1:
        pairs = 0
        for i in range(1,7):
            if(throw.count(i) >= 2):
                pairs += 1
        if (pairs == 1):
            possible += 1

    return possible

def initial_0():
    possible = 0
    for throw in list1:
        pairs = 0
        for i in range(1,7):
            if(throw.count(i) >= 2):
                pairs += 1
        if (pairs == 0):
            possible += 1

    return possible

def tran_11():
    list3 = list(product(range(1,7), repeat=3))

    possible = 0
    for throw in list3:
        pairs = 0
        for i in range(1,6):
            if(throw.count(i) >= 2):
                pairs += 1
        if (pairs == 0):
            possible += 1
        if (throw.count(6) >= 2):
            possible += 1
    
    return possible

def tran_12():
    list3 = list(product(range(1,7), repeat=3))

    possible = 0
    for throw in list3:
        pairs = 0
        for i in range(1,6):
            if(throw.count(i) >= 2):
                pairs += 1
        if (pairs == 1):
            possible += 1
        if (throw.count(6) >= 2):
            possible -= 1
    
    return possible


print('initial 4: ', initial_4())
print('initial 2: ', initial_2())
print('initial 0: ', initial_0())
print('tran 11: ', tran_11())
print('tran 12: ', tran_12())



