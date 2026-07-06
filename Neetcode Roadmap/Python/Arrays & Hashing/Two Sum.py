'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. 

Example:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''

def twoSum(nums: list[int], target: int) -> list[int]:
    
    indexes = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                indexes = [j, i]

    return indexes
    

nums, target = [3,4,5,6], 7

print (twoSum(nums, target))