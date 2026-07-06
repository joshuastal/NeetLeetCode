"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
"""


def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # freq.items() -> converts the dictionary into a list of tuples, each tuple is a pair (element, frequency)
    # key = lambda x: x[1] -> tells the sorted method to look at index 1 of each tuple (the frequency) when deciding the order
    # reverse = true -> reverse the order (largest to smallest)

    return [num for num, _ in sorted_freq[:k]]
    # num for... -> list comprehension that extracts just the num values and packages them into a new list
    # ...for num, _ in -> uses tuple unpacking. for each tuple, assigns the first value (the number) to num and ignores the second value
    # by assigning it to the throwaway variable _
    # sorted_freq[:k] -> slices the sorted list to keep only the first k tuples


nums = [1, 2, 2, 3, 3, 3]
print(topKFrequent(nums, 2))

nums = [7, 7]
print(topKFrequent(nums, 1))
