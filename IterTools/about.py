# IterTools
import itertools as it

# Counting values

'''
n = it.count(0, 5)

for i in n:
    print(i)
'''

# Into Cycle
'''
n = it.cycle('DOTKET')

for i in n:
    print(i)
'''    

# Repeat

'''
n = it.repeat('I am the best', 10)

for i in n:
    print(i)
'''
    
# Accumulate

'''    
n = it.accumulate([i for i in range(0, 10)])

for i in n:
    print(i)
'''

# Chain

'''
n = it.chain('Gabriel ', [' ', 1, 23, 10, ' '], ('Oi', 'Hello'))

for i in n:
    print(i)
'''



