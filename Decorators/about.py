# Decorators
# @decorators

# Call function into of other function and validate

# high order function 

def validate(func):
    def valid(x, y):
        if x < 0 or y < 0:
            raise ValueError('ERROR')
        return func(x, y)
    
    return valid

@validate
def sum(n1, n2):
    return n1 + n2

print(sum(10, 10))