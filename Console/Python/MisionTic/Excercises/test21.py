"""
    Serie fibonacci, con operadores for
"""

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

for i in range(100):
    print(fib(i))
