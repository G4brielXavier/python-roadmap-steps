#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ List Comprehension ============

ns_core = [5, 2, 7, 6, 8, 9, 12, 2, 11, 2, 3, 7, 723, 65, 77, 87, 98, 34]

# No Comprehension
for n in ns_core:
    if n > 5:
        print(n)
    
# Comprehension
ns_comp = [n * 2 for n in ns_core if n > 5]
print(ns_comp)

# Fibonacci
def fibonacci(n):
    a, b = 0, 1
    
    for _ in range(n):
        yield a
        a, b = b, a+b
        
fib = fibonacci(20)

for n in fib:
    print(n)