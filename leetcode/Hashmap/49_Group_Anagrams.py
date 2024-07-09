'''
Type : medium

Problem statement:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 
'''
class group_anagram:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s not in d:
                d[s]=[i]
            else:
                d[s].append(i)
        return list(d.values())
    
solution=group_anagram()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))