#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Recursion in python ============

def validation():
    value = input('Name: ')
    if value == 'Gabriel':
        return value
    
    #Recursion here
    validation()
    
name = validation()


    