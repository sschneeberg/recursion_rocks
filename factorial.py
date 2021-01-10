# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def memoized(f):
    import functools
    cached = dict()
    @functools.wraps(f)
    def wrapper(*args):
        if args not in cached:
            cached[args] = f(*args)
        return cached[args]
    return wrapper

@memoized
def factorial(n):
    if n < 0 : raise ValueError("n must be a positive integer")
    if type(n) != int : raise ValueError("n must be an integer")
    if 0 <= n < 2 : return 1
    else: 
        print(n)
        return n * factorial(n-1)

assert(factorial(0) == 1)
assert(factorial(5) == 120)
assert(factorial(8) == 40320)
# assert(factorial(-2) == 1) #should raise error
# assert(factorial(1.4) == 1) #should raise error