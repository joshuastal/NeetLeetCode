'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example:
Input: s = "racecar", t = "carrace"

Output: true
'''


def isAnagram( s: str, t: str) -> bool:
    sChars = {}
    tChars = {}

    for char in s:
        if char not in sChars:
            sChars[char] = 1
        sChars[char] += 1

    for char in t:
        if char not in tChars:
            tChars[char] = 1
        tChars[char] += 1

    if sChars == tChars:
        return True
    else:
        return False
    
#==========================================================================================#

def isAnagramAlternative( s: str, t: str) -> bool:
    sChars = list(s)
    tChars = list(t)

    sChars.sort()
    tChars.sort()

    if sChars == tChars:
        return True
    return False

#==========================================================================================#

s = "racecar"
t = "carrace"

print(isAnagram(s, t))


