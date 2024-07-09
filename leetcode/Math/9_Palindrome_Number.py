'''
Type :easy

Problem statement:

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
class palindrome_number:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x!=0 and x%10==0):
            return False
        rev=0
        while(x>rev):
            rev=rev*10+x%10
            x=x//10
        if((x==rev)or(x==rev//10)):
            return True
        else:
            return False
        
solution=palindrome_number()
print(solution.isPalindrome(121))
        