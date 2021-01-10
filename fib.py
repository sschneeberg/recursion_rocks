# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1

def memoized(f):
    cached = dict()
    import functools
    @functools.wraps(f)
    def wrapper(*args):
        if args not in cached:
            cached[args] = f(*args)
        return cached[args]
    return wrapper

@memoized
def fib(n):
    if type(n) != int : raise ValueError("n must be a positive integer")
    if n <= 0 : return 0
    if n < 2: return 1
    else : return fib(n-1) + fib(n-2)

# print(fib(-1))
# => 0
# print(fib(0))
# => 0
# print(fib(1))
# => 1
# print(fib(2))
# => 1
# print(fib(7))
# => 13

assert(fib(-1) == 0)
assert(fib(0) == 0)
assert(fib(1) == 1)
assert(fib(2) == 1)
assert(fib(7) == 13)
# assert(fib('s') == 0) #should raise error