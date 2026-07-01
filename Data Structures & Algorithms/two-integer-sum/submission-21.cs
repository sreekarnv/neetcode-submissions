public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] result = {-1, -1};
        Dictionary<int, int> mapper = new Dictionary<int, int> {};

        for(int i = 0; i < nums.Length; i++)
        {
            int m = target - nums[i];
            if (mapper.ContainsKey(m))
            {
                result[0] = mapper[m];
                result[1] = i;
                break;
            }

            mapper[nums[i]] = i;
        }

        return result;
    }
}
