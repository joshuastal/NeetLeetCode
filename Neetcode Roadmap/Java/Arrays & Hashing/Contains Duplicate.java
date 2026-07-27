/*
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
*/
import java.util.HashMap;

class ContainsDuplicateSolution {

  public boolean containsDuplicate(int[] nums) {
    HashMap<Integer, Integer> seen = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      if (!seen.containsKey(nums[i])) {
        seen.put(nums[i], 0);
      } else {
        return true;
      }
    }
    return false;
  }
}
