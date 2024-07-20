#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Decorators ============

# @decorators

# Call function into of other function and validate

# high order function 

def validate_username(func):
    def valid(name):
        length_name = len(name)
        if not length_name > 4:
            print('Length username not accepted')
            return
        print('Accepted username')
        return func(name)
    return valid

@validate_username
def return_username(name):
    return name

edit_profile_name = input('Username: ')
profile_name = return_username(edit_profile_name)