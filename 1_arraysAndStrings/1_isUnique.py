"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

def isUniqueOnHashtable(str):				# time O(N) | space O(N) - need to create a hashtable
    uniques = {}
    for char in str:
        if char in uniques:
            return False
        else:
            uniques[char] = 1
    return True

def isUniqueOnSet(str):						# time O(N) | space O(N) - need to create a set
    return len(str) ==len(set(str))


def isUnique(str):							# time O(N log N) | space O(N) - need to create an array
    arr = sorted(str)
    current_char = ''
    for char in arr:
        if char == current_char:
            return False
        else:
            current_char = char
    return True

def isUniqueBitwise(str):					# time O(N) | space O(1) - need to checker, where 1 << current_bit will set current bit to 1
	checker = 0   # 32 bits set to 0 if a-z string
    for char in str:
        currentBit = ord(char) - ord('a')
        if (checker & (1 << currentBit)) > 0:
            return False
        checker |= (1 << currentBit)
         
    return True

print(isUnique("abac"))
print(isUnique("abc"))
