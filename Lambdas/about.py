#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Lambdas ============

# Uma função normal que descobre a idade pela data de nascimento e o ano atual

def validate_year(func):
    def valid(born_year, current_year):
        if current_year > 2024:
            return False
        
        return func(born_year, current_year)
    
    return valid

@validate_year
def find_year(born_year, current_year):
    return current_year - born_year

myAge = find_year(2006, 2026)

# function lambda that does same thing

find_year_lambda = lambda born_year, current_year : current_year - born_year
myAge_lambda = find_year_lambda(2006, 2026)
print(myAge_lambda)