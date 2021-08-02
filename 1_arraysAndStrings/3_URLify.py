"""
1.3 URLify: Write a method to replace all spaces in a sring with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string
"""

def URLify(str):				# time O(N) | space O(N) - for array and another one for the result string
    result = []
    for char in str.strip():
        if (char == ' '):
            result += '%20'
        else:
            result += char
    return "".join(result)


def URLifyFast(str):			# time O(N) | space O(1) - python inplace algorithms
	return str.strip().replace(' ', "%20")



print(URLify("Mr John Smith    "))
