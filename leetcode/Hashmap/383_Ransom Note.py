'''

Type : Easy

Problem statement:

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the 
letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote. 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
'''
    
class ransom_note:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}
        for c in magazine:
            if c in counter:
                counter[c]+=1
            else:
                counter[c]=1
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c]==1:
                del counter[c]
            else:
                counter[c]-=1
        return True

        


# Test the function
solution = ransom_note()
print(solution.canConstruct("aa", "aab"))