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

"""
Book comments:
- confirm with interviewer if solution is case sensitive

Book solution in Java

// sort the strings                         # time O(N log N) | space O(1)
String sort(String s) {
    char[] content = s.toCharArray();
    java.util.Arrays.sort(content);
    return new String(content);
}

boolean permutation(String s, String t) {
    if (s.length() != t.length()) {
      return false;
    }
    return sort(s).equals(sort(t));
}

// check if two strings have identical character counts
boolean permutation(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] letters = new int[128]
    for (int i = 0; i < s.length(); i++) {
      letters[s.charAt(i)]++;
    }
    for (int i = 0; i < t.length(); i++) {
      letters[t.charAt(i)]--;
      if (letters[t.charAt(i)] < 0) {
        return false;
      }
    }
    return true;
}
"""
