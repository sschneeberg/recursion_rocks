# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a function that accepts a complex dictionary and prints out all of it's keys and all of its values. 
# The dictionary can have dictionaries nested inside of it
# 'dictionary' is the dictionary that's currently being iterated over.
# 'indent' is a string representing the current level of indentation
# ...
# pretty_print(inner_dictionary, indent + '..');
# ...

def pretty_print(dictionary, indent, level=1):
    if type(dictionary) != dict : raise ValueError("can only pretty print dictionaries")
    pretty = ""
    for key in dictionary:
        val = dictionary[key]
        if type(val) != dict: 
            pretty = pretty + f"{indent*level}{key}: {val}\n"
        else:
            pretty = pretty + f"{indent*level}{key}: \n" + pretty_print(val, indent, level + 1)
    return pretty

o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

print(pretty_print(o1, "-"))
# -a: 1
# -b:2
print(pretty_print(o2, " "))
# a: 1
# b: 2
# c:
#  name: Bruce Wayne
#  occupation: Hero
# d: 4
print(pretty_print(o3, ".."))
# ..a: 1
# ..b: 2
# ..c:
# ....name: Bruce Wayne
# ....occupation: Hero
# ....friends: 
# ......spiderman:
# ........name: Peter Parker
# ......superman: 
# ........name: Clark Kent
# ..d: 4
# print(pretty_print([1,2], "--")) #should raise value error