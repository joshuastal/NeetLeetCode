/*
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
*/
import java.util.Arrays;

class Solution {

  public String[] fizzBuzz(int num) {
    String[] result = new String[num];

    for (int i = 1; i <= num; i++) {
      if ((i % 3 == 0) & (i % 5 == 0)) {
        result[i - 1] = "FizzBuzz";
      } else if (i % 3 == 0) {
        result[i - 1] = "Fizz";
      } else if (i % 5 == 0) {
        result[i - 1] = "Buzz";
      } else {
        result[i - 1] = String.valueOf(i);
      }
    }

    return result;
  }
}

class FizzBuzz {

  public static void main(String[] args) {
    Solution fizzBuzz = new Solution();

    System.out.println(Arrays.toString(fizzBuzz.fizzBuzz(15)));
  }
}
