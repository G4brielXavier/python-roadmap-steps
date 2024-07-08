#Type Castings and Exceptions

#----Type Castings
# Conversions of values, changes of types


# Implicit
n = 5

# Explicit
n_float = float(n)
n_string = str(n)
n_boolean = bool(n)
n_integer = int(n)

# Exceptions

#Type Exceptions
# ValueError, ImportError, TypeError and etc

# try, except, finally

try:
    print(5 + '5') # Adding a variable of type integer with a variable of type string
except Exception as err:
    print(f'Ops, ocorred a error - {err}')
    
    



