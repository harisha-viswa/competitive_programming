'''
Type : Easy

Problem statement:

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

'''
class contains_duplicate_2:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d={}
        for index,num in enumerate(nums):
            if num not in d:
                d[num]=index
            else:
                prev_i=d[num]
                curr_i=index
                diff=abs(prev_i-curr_i)
                if(diff<=k):
                    return True
                else:
                    d[num]=index

solution=contains_duplicate_2()
print(solution.containsNearbyDuplicate([1,0,1,1],1))