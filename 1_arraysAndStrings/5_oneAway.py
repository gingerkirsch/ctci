"""
1.5 One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away
"""

def isOneAway(str1, str2):						# time O(N) | space O(1)
    n = len(str1)
    m = len(str2)
    if (abs(n - m) > 1):
        return False
    edits = 0
    i = 0
    j = 0
    while i < n and j < m:
        if str1[i] != str2[j]:
            if edits == 1:
                return False
            if n > m:
                i+=1
            elif m > n:
                j+=1
            else:
                i+=1
                j+=1
            edits+=1
        else:
            i+=1
            j+=1
    if i < n or j < m:
        edits +=1
 
    return edits == 1
	
	
print(isOneAway("pale", "ple"))
print(isOneAway("pales", "pale"))
print(isOneAway("pale", "bale"))
print(isOneAway("pale", "bake"))
print(isOneAway("pale", "pl"))
