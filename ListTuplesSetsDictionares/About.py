#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Lists, Tuples, Sets and Dictionaries ============

# List - Normal list
numbers_list = [2, 6, 7, 2, 8.4, 9, 10, 22.2, 1, 2.1, 3.7, 4, 54]
strings_list = ['horse', 'cats', 'dogs', 'pigs', 'rabbit']
compound_list = [[18, 1.82], [15, 1.74]]

# Tuples - List with value immutables
numbers_tuple = (2, 3, 45, 7, 4, 3, 5, 8, 9, 10)

# Sets - List with values in ascending order and different values 
numbers_sets = {2, 3, 1, 6, 7, 8, 9, 2, 1}

#Dictionaries - List with value that have identifier, callable 'keys', each key have a value 
peoples_names = {
    'people_1':'Gabriel',
    'people_2':'João',
    'people_3':'Carlos',
    'people_4':'Laura'
}



# --- Controlling List

# Normal list can be changes
numbers_list[10] = 'Oi'
# Tuples values can't be changes
# numbers_tuple[10] = 'Oi'

# --- Controlling Dictionaries
peoples_names.items()
peoples_names.values()
peoples_names.keys