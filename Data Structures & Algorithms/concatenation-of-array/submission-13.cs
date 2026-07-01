public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int originalLength = nums.Length;
        Array.Resize<int>(ref nums, 2 * originalLength);

        for (int i = originalLength; i < nums.Length; i++)
        {
            nums[i] = nums[i - originalLength];
        }

        return nums;
    }
}