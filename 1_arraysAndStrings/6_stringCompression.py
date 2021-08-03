"""
1.6 String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. 
If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z)
"""

def stringCompression(input):						# time O(N) | space O(N)
    current_char = ''
    count = 0
    compressed = []
    for char in input:
        if (char != current_char):
            if (count != 0):
                compressed.append(current_char)
                compressed.append(str(count))
            current_char = char
            count = 1
        else:
            count += 1
    compressed += current_char
    compressed += str(count)
    
    if (len(compressed) > len(input)):
        return input
    else:
        return "".join(compressed)
		
print(stringCompression("aabcccccaa"))