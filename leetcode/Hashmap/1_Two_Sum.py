'''

Type : easy

Problem statement:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 '''

class two_sum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d={}
        for i in range(0,len(nums)):
            value=nums[i]
            difference=target-value
            if value not in d:
                d[difference]=i
            else:
                current_index=i
                previous_index=d[value]
                return  [current_index,previous_index]
        return[]
solution=two_sum()
print(solution.twoSum([2,7,11,15],9))
               