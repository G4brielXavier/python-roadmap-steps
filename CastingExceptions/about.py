#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Type Casting and Exceptions ============

#----Type Castings
# Conversions of values, changes of types


# Implicit
n = 5

# Explicit
n_float = float(n) # 5.0
n_string = str(n) # '5'
n_boolean = bool(n) # True
n_integer = int(n) # 5
n_binary = bin(n) # 0b0101010111
n_hexadecimal = hex(n) # 0x12345 
n_octal = oct(n) # 0o77723

# Exceptions

#Type Exceptions
# ValueError, ImportError, TypeError and etc

# try, except, finally

try:
    print(5 + 5) # Adding a variable of type integer with a variable of type string
    x = int(input('n: '))
except ValueError: 
    print(f'Value error')
except TypeError:
    print(f'Type error')
finally:
    print('Thank you for test')