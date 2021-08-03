"""
1.3 URLify: Write a method to replace all spaces in a sring with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string
"""

def URLify(str):				# time O(N) | space O(N) - for array and another one for the result string
    result = []
    for char in str.strip():
        if (char == ' '):
            result.append('%20')
        else:
            result.append(char)
    return "".join(result)


def URLifyFast(str):			# time O(N) | space O(1) - python inplace algorithms
	return str.strip().replace(' ', "%20")



print(URLify("Mr John Smith    "))

"""
Book comments:
 - common approach: edit the string starting from the end and working backwards:
   - we count the number of spaces
   - we need two extra characters for each space
   - walk backwards editing it

Book solution in Java

void replaceSpaces(char[] str, int trueLength) {
    int numberOfSpaces = countOfChar(str, 0, trueLength, ' ');
    int newIndex = trueLength - 1 + numberOfSpaces * 2;
    // if there are excess spaces, add a null character
    if (int oldIndex = trueLength - 1; oldIndex >= 0; oldIndex -=1) {
      if (str[oldIndex] == ' '){
        str[newIndex] = '0';
        str[newIndex - 1] = '2';
        str[newIndex - 2] = '%';
        newIndex -=3;
      } else {
        str[newIndex] = str[oldIndex];
        newIndex -= 1;
      }
    }
}

int countOfChar(char[] str, int start, int end, int target) {
    int count = 0;
    for (int i = start; i < end; i++) {
      if (str[i] == target) {
        count++;
      }
    }
    return count;
}
"""
