#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Generator Expressions ============

# List Comprehension
comprehension = [n * 2 for n in range(100)]

# Generator Expression
generator = (n * 2 for n in range(100))

for x, y in enumerate(generator):
    print(f'{x} : {y}')

# yield

def generator_yield(limit):
    for x in range(1, limit):
        if x % 2 == 0:
            yield x
    
