"""
Given an array of integers, return a list of products where output[i] is the product of all elements except nums[i]

Example 1:
    Input: nums = [1,2,4,6]

    Output: [48,24,12,8]

Example 2:
    Input: nums = [-1,0,1,2,3]

    Output: [0,-6,0,0,0]

https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    products = []
    product = 1

    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        products.append(product)
        product = 1

    return products


print(productExceptSelf([1, 2, 4, 6]))
print(productExceptSelf([-1, 0, 1, 2, 3]))
