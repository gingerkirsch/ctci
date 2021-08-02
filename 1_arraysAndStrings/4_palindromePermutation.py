"""
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to jsut dictionary words.
You can ignore casing and non-letter characters.
"""
from math import ceil

def isPalindromePermutation(str):						# time O(N) | space O(N) - need to create a set
	clean = ''.join(ch for ch in str if ch.isalpha()).lower()
	return len(set(clean)) == ceil(len(clean) / 2)

def isPalindromePermutationBitwise(str):				
	clean = ''.join(ch for ch in str if ch.isalpha()).lower()
    checker = 0
    for char in clean:
        checker ^= 1 << ord(char)
    return checker == 0 or checker & (checker - 1) == 0


print(isPalindromePermutation("Tact Coa"))
