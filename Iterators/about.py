#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Iterators ============

# Example of iterators
# list, dictionaries, tuples, sets, strings

#Iterating for a list
numbers = [5, 6, 1, 2, 8, 9]

for i in numbers:
    print(i)
    

#Iterating for a dictionarie
info = {
    'name':'Gabriel',
    'age':18,
    'genrer':'Male'
}

for i, v in info.items():
    print(f'{i} - {v}')
    

#Iterating for a tuples and sets 
tupl = (6, 4, 2, 1, 6, 7, 8)
sets = {6, 7, 2, 3, 1, 5, 6}

for i in tupl:
    print(i)
    
for i in sets:
    print(i)
    
#Iterating for a string
for i in 'Gabriel':
    print(i)