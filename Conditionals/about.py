#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Conditionals and Operators ============

#if, else, elif
n1 = 10

if n1 == 10:
    print('yes')
elif n1 < 2:
    print('ok')
else:
    print('no')

#Operators

#Arithmetics
# + - * / // ** %
print(5 + 5) # Adding
print(5 - 5) # Subtration
print(5 * 5) # Multiplication
print(5 / 5) # Division
print(5 // 5) # Integer Division
print(5 ** 2) # Power
print(5 % 2) # Module ( return rest of a division )

#Relationals
# And Or not is

n2 = 5
is_okay = False

if is_okay is True:
    print('Ok')
elif not is_okay is True:
    print('Ok, no')

if n1 > 10 and n2 < 4:
    print('Yes')
elif n1 > 5 or n2 > 2:
    print('Ok')
else:
    print('No')

#Logicals
# < > => <= == !=

if n1 >= n2 or n1 <= n2:
    print('Ok')
elif n2 != 2 and n1 > 3:
    print('Yes')