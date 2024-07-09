'''
Type : Easy

Problem statement:

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class isomorphic:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range (len(s)):
            char1,char2=s[i],t[i]
            if char1 not in d:
                if char2 in d.values():
                    return False
                d[char1]=char2
            elif d[char1]!=char2:
                return False
        return True
    

solution = isomorphic()
print(solution.isIsomorphic("egg","add"))