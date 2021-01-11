# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    # Edge case and base case:
    if len(ss) == 0 or len(ss) == 1: return ss
    else: return reverse(ss[1:]) + ss[0]

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"



assert(reverse("") == "")
assert(reverse("a") == "a")
assert(reverse("computer") == "retupmoc")
assert(reverse("I put my thing down flip it and reverse it") == "ti esrever dna ti pilf nwod gniht ym tup I")
