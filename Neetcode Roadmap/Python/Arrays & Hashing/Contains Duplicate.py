'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''

input = [1, 2, 3, 4]

def containsDuplicate(numbers: list[int]) -> bool:
    duplicates = {}
    for num in numbers:
            if num in duplicates:
                    return True
            duplicates[num] = num
    return False


print(containsDuplicate(input))