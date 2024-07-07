# Decorators
# @decorators

# Call function into of other function and validate

def validate(func):
    def valid(n1, n2):
        if n1 < 0 or n2 < 0:
            raise ValueError('n1 or n2 can not be negative')
        
        return func(n1,n2)
    
    return valid


@validate # <<<<
def sum(n1, n2):
    return n1 + n2 

print(sum(10, 2))


