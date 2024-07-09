'''
Type : Easy

Problem statement:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 

'''
class anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for c in t:
            if c in d:
                d[c]+=1
            else:
               d[c]=1
        for c in s:
            if c not in d:
                return False
            elif d[c]==1:
                del d[c]
            else:
                d[c]-=1
        return True
    
Solution=anagram()
print(Solution.isAnagram("anagram","nagaram"))