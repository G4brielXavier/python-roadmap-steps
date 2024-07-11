# IterTools - Library to control value whatever iterable

import itertools as it

# Counting values

'''
n = it.count(0, 1)

for i in n:
    print(i)
'''

# Into Cycle

'''
n = it.cycle('DOTKET')

for i in range(len('DOTKET')):
    print(next(n))
    
'''
# Repeat


'''
n = it.repeat('I am the best', 10)

for i in range(10):
    print(next(n))
'''

    
# Accumulate
 
'''
n = it.accumulate([i for i in range(10)])

for i in range(10):
    print(next(n))
'''

# Chain

'''
n = it.chain('Gabriel ', [' ', 1, 23, 10, ' '], ('Oi', 'Hello'))

for i in n:
    print(i)
'''

# Compress

'''
from random import choice
n = it.compress([i for i in range(10)], [choice([0, 1]) for _ in range(10)])
print(list(n))
'''

# Product

'''
n = it.product('gabriel', repeat=2)
print(list(n))
'''

# Permutations

'''
n = it.permutations('gabriel', 2)
print(list(n)
'''

#Combinations

'''
n = it.combinations('gabriel', 2)
print(list(n))
'''
