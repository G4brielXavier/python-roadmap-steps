#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Lists, Tuples, Sets and Dictionaries ============

# List - Normal list
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tuples - List with value immutables
numbers_tuple = (2, 3, 45, 7, 4, 3, 5, 8, 9, 10)

# Sets - List with values in ascending order and different values 
numbers_sets = {2, 3, 1, 6, 7, 8, 9, 2, 1}


#Dictionaries - List with value that have identifier, callable 'keys', each key have a value 
from random import randint

values = {v:0 for v in range(50)}

for i, v in values.items():
    values[i] = randint(10, 100)
    
for i, v in values.items():
    print(f'{i} - {v}')

# --- Controlling List

# Normal list can be changes
# Tuples values can't be changes
# numbers_tuple[10] = 'Oi'

# --- Controlling Dictionaries
values.items()
values.values()
values.keys()