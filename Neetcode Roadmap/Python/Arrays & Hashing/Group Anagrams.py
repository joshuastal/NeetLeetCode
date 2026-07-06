'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]
'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    

    for string in strs:
        key = tuple(sorted(string)) # use a tuple for the key, since it is immutable and can be used as a key
                                    # lists cannot be used as a key since they are mutable

        if key not in result:
            result[key] = []
        
        result[key].append(string)


    return list(result.values())


strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]