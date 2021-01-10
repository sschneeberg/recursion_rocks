# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    if type(l[0]) != int: raise ValueError("l must be a list of integers")
    if len(l) <= 1: return 1
    else: return max(l[0], find_max(l[1:]))

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

assert(find_max([1, 4, 45, 6, -50, 10, 2]) == 45)
assert(find_max([3,4,-5,7,23,89,23542345,85,3234,43]) == 23542345)
# assert(find_max([1,5,'a']) == 0) #should raise error