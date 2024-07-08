# Lambdas

# normal function that sum two values

def sum(n1, n2):
    return n1 + n2

res = sum(10, 20)

print(f'Using normal function: {res}')

# function lambda that does same thing

res_lbd = lambda n1, n2: n1 + n2

print(f'Using lambda: {res_lbd(10, 20)}')