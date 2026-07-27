/*
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example:
Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
*/

class TwoSumSolution {

  public int[] twoSum(int[] nums, int target) {
    int[] indices = new int[2];

    for (int i = 0; i < nums.length; i++) {
      for (int j = 0; j < nums.length; j++) {
        if (i != j && nums[i] + nums[j] == target) {
          indices[0] = j;
          indices[1] = i;
        }
      }
    }

    return indices;
  }
}
