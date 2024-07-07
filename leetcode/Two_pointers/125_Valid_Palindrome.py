'''

Type : Easy

Problem statement:

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
class valid_palindrome:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s2=''.join(ch for ch in s if ch.isalpha()or ch.isnumeric())
        lasti=len(s2)-1
        line=len(s2)//2
        for i in range (0,line):
            if s2[i]!=s2[lasti-i]:
                return False
        return True 
    

solution=valid_palindrome()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))