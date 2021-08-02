"""
1.2 Check Permutations: Given two strings, write a method to decide if one is a permutation of the other.
"""

def isPermutation(str1, str2):				# time O(N log N) | space O(1) 
    return sorted(str1) == sorted(str2)

def isPermutation(str1, str2):				# time O(N) | space O(N) - to create a hashtable
    chars = {}
    for char in str1:
        if (char not in chars):
            chars[char] = 0
        chars[char] += 1
    for char in str2:
        if (char not in chars):
            chars[char] = 0
        chars[char] -= 1
    for value in chars.values():
        if value != 0:
            return False
    return True

print(isPermutation("abac", "cbaa"))
print(isPermutation("abac", "cbada"))
