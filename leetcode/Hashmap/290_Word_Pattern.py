'''
Type : Easy

Problem statement:

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''


class word_pattern:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        d={}
        for i in range (len(pattern)):
            char1,char2=pattern[i],s[i]
            if char1 not in d:
                if char2 in d.values():
                    return False
                d[char1]=char2
            elif d[char1]!=char2:
                return False
        return True
    
Solution=word_pattern()
print(Solution.wordPattern("abba","dog cat cat dog"))
        