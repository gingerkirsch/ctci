"""
1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
Given two  strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
"""

def rotation(s1,s2):						# time O(N) | space O(N) - bunch of substrings
    if (len(s1) != len(s2)):
        return s1
    i = 0
    j = 0
    while (s1[i] != s2[j]):
        i += 1
    return s1[i:] + s1[:i]
            
print(rotation("waterbottle","erbottlewat") in "erbottlewat")
print(rotation("waterbattle","erbottlewat") in "erbottlewat")
