"""
Make a program to encode a LIST of strings into ONE string. The encoded string is then sent over the network and decoded back into the original list of strings.

Example 1:
    Input: dummy_input = ["Hello","World"]

    Output: ["Hello","World"]


Example 2:
    Input: dummy_input = [""]

    Output: [""]


https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150
"""


def encode(self, strs: list[str]) -> str:
    encoded_string = "".join(f"{len(s)}#{s}" for s in strs)
    # put the length of the string followed by a # to the front of it
    # ["lint", "code", "love", "you"] -> 4#lint4#code4#love3#you
    # if a string contains # then its okay because the program will read the next n characters anyways

    # for string in strs:
    #     encoded_string += (str(len(string)) + "#" + string)
    #
    # this was my original solution, but because strings in python are immutable, each time it would have to create a new string object
    # and copy the original content over to the new string object on each iteration

    return encoded_string


def decode(self, s: str) -> list[str]:
    results = []
    i = 0

    while i < len(s):
        j = i

        # j finds the # while i finds the index
        while s[j] != "#":
            j += 1

        # the length is the string starting at i and ending at j (exclusive)
        # 10# -> 10
        length = int(s[i:j])

        # once delimitter is found, string starts after j and goes its entire length (obviously)
        string_content = s[j + 1 : j + 1 + length]
        results.append(string_content)

        i = j + 1 + length  # jump to next string

    return results
