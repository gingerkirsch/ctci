"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

def isUniqueOnHashtable(s):				# time O(N) | space O(N) - need to create a hashtable
    uniques = {}
    for char in s:
        if char in uniques:
            return False
        else:
            uniques[char] = 1
    return True

def isUniqueOnSet(str):						# time O(N) | space O(N) - need to create a set
    return len(s) ==len(set(s))


def isUnique(s):							# time O(N log N) | space O(N) - need to create an array
    arr = sorted(s)
    current_char = ''
    for char in arr:
        if char == current_char:
            return False
        else:
            current_char = char
    return True

def isUniqueBitwise(s):					# time O(N) | space O(1) - need to checker, where 1 << current_bit will set current bit to 1
	checker = 0   # 32 bits set to 0 if a-z string
    for char in s:
        currentBit = ord(char) - ord('a')
        if (checker & (1 << currentBit)) > 0:
            return False
        checker |= (1 << currentBit)
         
    return True

print(isUnique("abac"))
print(isUnique("abc"))


"""
Book comments:
1) ask if the string is ASCII
2) if length > 128 then not unique (256 - extended ASCII)

Book solution in Java

boolean isUniqueChars(String str){              # time O(N) | space O(1) * 128
    if (str.length() > 128) return false;

    boolean[] char_set = new boolean[128];
    for (int i = 0;, i < str.length(); i++) {
      int val = str.charAt(i);
      if (char_set[val]){
        return false;
      }
      char_set[val] = true;
    }
    return true;
}


boolean isUniqueChars(String str){              # time O(N) | space O(1)
    int checker = 0;
    for (int i = 0; i < str.length(); i++) {
      int val = str.charAt(i) - 'a';
      if ((checker & (1 << val)) > 0) {
        return false;
      }
      checker |= (1 << val)
    }
    return true;
}
"""
