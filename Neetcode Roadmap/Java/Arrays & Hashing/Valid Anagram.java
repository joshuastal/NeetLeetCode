/*
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example:
Input: s = "racecar", t = "carrace"

Output: true
*/

import java.util.Arrays;

class ValidAnagramSolution {

  public boolean isAnagram(String s, String t) {
    s = s.toLowerCase();
    t = t.toLowerCase();

    char[] sChars = s.toCharArray();
    char[] tChars = t.toCharArray();

    Arrays.sort(sChars);
    Arrays.sort(tChars);

    if (Arrays.equals(sChars, tChars)) {
      return true;
    }
    return false;
  }
}
