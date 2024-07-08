#Conditionals

#if, else, elif
n1 = 10
if n1 > 5: 
    print('Yes')
elif n1 < 5:
    print('Ok')
else:
    print('No')

#Operators

#Arithmetics
# + - * / // ** %
print(5 + 5) # Adding
print(5 - 5) # Subtration
print(5 * 5) # Multiplication
print(5 / 5) # Division
print(5 // 5) # Integer Division
print(5 ** 2) # Power
print(5 % 2) # Return Rest Division

#Relationals
# And Or not is
n2 = 5
is_okay = False

if is_okay is True:
    print('Ok')

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
