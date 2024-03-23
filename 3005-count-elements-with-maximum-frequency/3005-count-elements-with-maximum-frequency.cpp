class Solution {
public:
    int maxFrequencyElements(vector<int>& nums)
    {
        int count = 0;
        vector<int> fr(nums.size(), 0); // Initialize frequency vector with zeros

        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {
                if (nums[i] == nums[j])
                    fr[i]++;
            }
        }

        int max_freq = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (fr[i] > max_freq)
                max_freq = fr[i];
        }

        for (int i = 0; i < nums.size(); i++)
        {
            if (fr[i] == max_freq)
                count++;
        }

        return count;
    }
};