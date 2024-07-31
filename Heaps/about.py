#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Heaps ============

#import the library

import heapq as hp

#create a list of numbers

numbers = [i for i in range(1, 10+1)]

#transforming normal list to heap

hp.heapify(numbers)

#push 100 in list numbers 

hp.heappush(numbers, 100)

#pop in smaller value in numbers

hp.heappop(numbers)

#push 542 and pop in smaller value of numbers

hp.heappushpop(numbers, 542)

#pop and return the smaller value and add a new element "656"

smaller = hp.heapreplace(numbers, 656)
print(f'The smaller value is {smaller}')

#return the smallers values

three_smallers_value = hp.nsmallest(3, numbers)
print(f'The Three smallers value is {three_smallers_value}')

#return the largest values

three_largest_value = hp.nlargest(3, numbers)
print(f'The Three largests value is {three_largest_value}')

#merging two heaps

numbers_one = [1, 2, 3]
numbers_two = [4, 5, 6]

numbers_three = list(hp.merge(numbers_one, numbers_two))
print(numbers_three)