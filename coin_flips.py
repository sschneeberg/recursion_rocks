# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def memoized(f):
    import functools
    cached = dict()
    @functools.wraps(f)
    # wrap function and add reuslts to cached if not already cached
    def wrapper(*args):
        if args not in cached:
            cached[args] = f(*args)
        return cached[args]
    return wrapper

def strMult(val, array):
    newArr = []
    for i in range(len(array)):
        newArr.append(array[i] + val)
    return newArr

@memoized
def coin_flips(n):
    print(n)
    # Base case: 
    if n == 1 : return ['H', 'T']
    else: 
        # return H*coin_flips(n-1) + T*coin_flips(n-1)
        return strMult('H', coin_flips(n-1)) + strMult('T', coin_flips(n-1))

assert(set(coin_flips(2)) == set(["HH", "HT", "TH", "TT"]))
assert(set(coin_flips(4)) == set(["HHHH", "HHHT", "HHTT", "HTTT", "HHTH", "HTHH", "THHH", "TTHH", "TTTH" , "TTTT", "THTH", "THHT", "HTHT", "HTTH", "TTHT", "THTT"]))

