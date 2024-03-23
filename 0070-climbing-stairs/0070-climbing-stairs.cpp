
#include <unordered_map>

class Solution {
public:
    int climbStairs(int n) {
        std::unordered_map<int, int> memo;
        return climbStairsHelper(n, memo);
    }
    
    int climbStairsHelper(int n, std::unordered_map<int, int>& memo) {
        if (n <= 2)
            return n;
        
        if (memo.find(n) != memo.end())
            return memo[n];
        
        int result = climbStairsHelper(n-1, memo) + climbStairsHelper(n-2, memo);
        memo[n] = result;
        
        return result;
    }
};