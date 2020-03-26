
# extra_end
def extra_end(str):
    if len(str) <= 2:
        return str + str + str
    else:
        newStr = str[len(str) - 1] +  str[len(str) - 2]
        return newStr + newStr + newStr
print(extra_end("hello"))

# Given a string, return the string made of its first two chars,
# so the String "Hello" yields "He". If the string is shorter than length 2,
#return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
    if len(str) <= 2:
        return str
    else:
        str = str[0] + str[1]
        return str
print(first_two("hello"))

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    half = len(str) / 2
    return str[0:half]

print(first_half('WooHoo'))

# Given a string, return a version without the first and last char,
# so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
    return str[1: len(str) - 1]

print(without_end("hello"))

# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).+
def combo_string(a, b):
    return  a + b + a if len(a) < len(b) else b + a + b

print(combo_string('Hello', 'hi'))


# Given 2 strings, return their concatenation,
# except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
    return a[1: len(a)] + b[1: len(b)]

print(non_start("hello", "there"))


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.

def leftTwo(str):
    newStr = str[2: len(str)]
    return newStr + str[0] + str[1]

print(leftTwo("Chocolate"))
