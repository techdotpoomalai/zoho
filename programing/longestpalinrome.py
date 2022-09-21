'''

Longest Palindrome in a String 
Medium Accuracy: 49.2% Submissions: 58402 Points: 4
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).


Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.

'''

class solution:
    def longest_palin(self, s):
        long_palin=''
        palin=''
        palin1=''
        palin_reverse=''
        for o in range(len(s)):
            palin+=s[o]
            if palin==palin[::-1] and len(long_palin) < len(palin):
                long_palin=palin
            else:
                palin_reverse=palin[::-1]
                for y in range(len(palin_reverse)):
                    palin1+=palin_reverse[y]
                    if palin1==palin1[::-1] and len(long_palin) < len(palin1):
                        long_palin=palin1
                palin1=''
                
        print(long_palin)
        
string="bannana"
sol=solution()
sol.longest_palin(string)